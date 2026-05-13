import base64
import asyncio
import io
import mimetypes
from pathlib import Path
from datetime import datetime

import anthropic
from dotenv import load_dotenv
from PIL import Image

from prompts import BLOG_AGENT_PROMPT, YOUTUBE_AGENT_PROMPT, INSTAGRAM_AGENT_PROMPT

load_dotenv()

CLIENT = anthropic.AsyncAnthropic()
MODEL = "claude-sonnet-4-6"
MAX_IMAGES = 20
MAX_IMAGE_DIMENSION = 1024


def resize_image(path: Path) -> tuple[str, str]:
    img = Image.open(path)
    img.thumbnail((MAX_IMAGE_DIMENSION, MAX_IMAGE_DIMENSION), Image.LANCZOS)
    buf = io.BytesIO()
    fmt = "JPEG" if path.suffix.lower() in {".jpg", ".jpeg"} else "PNG"
    img.save(buf, format=fmt, quality=80)
    mime = "image/jpeg" if fmt == "JPEG" else "image/png"
    return base64.standard_b64encode(buf.getvalue()).decode(), mime


def load_images(input_dir: Path) -> list[dict]:
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
    image_files = sorted(
        [f for f in input_dir.iterdir() if f.suffix.lower() in image_extensions]
    )
    if len(image_files) > MAX_IMAGES:
        print(f"  [주의] 이미지 {len(image_files)}장 중 {MAX_IMAGES}장만 사용 (균등 샘플링)")
        step = len(image_files) / MAX_IMAGES
        image_files = [image_files[int(i * step)] for i in range(MAX_IMAGES)]

    images = []
    for f in image_files:
        data, mime = resize_image(f)
        images.append({
            "type": "image",
            "source": {"type": "base64", "media_type": mime, "data": data},
        })
        print(f"  [이미지 로드] {f.name} (리사이즈 완료)")
    return images


def load_guide(input_dir: Path) -> str:
    for name in ["guide.txt", "가이드.txt"]:
        p = input_dir / name
        if p.exists():
            print(f"  [가이드 로드] {p.name}")
            return p.read_text(encoding="utf-8")
    txt_files = list(input_dir.glob("*.txt"))
    if txt_files:
        print(f"  [가이드 로드] {txt_files[0].name}")
        return txt_files[0].read_text(encoding="utf-8")
    raise FileNotFoundError("inputs/ 폴더에 텍스트 가이드 파일(.txt)이 없습니다.")


async def run_agent(name: str, system_prompt: str, user_content: list[dict]) -> str:
    print(f"\n  [{name}] 에이전트 시작...")
    response = await CLIENT.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    result = response.content[0].text
    print(f"  [{name}] 완료 (토큰: 입력 {response.usage.input_tokens}, 출력 {response.usage.output_tokens})")
    return result


async def run_pipeline(input_dir: Path, output_dir: Path):
    print("=" * 60)
    print("  F&B 콘텐츠 파이프라인 시작")
    print("=" * 60)

    guide_text = load_guide(input_dir)
    images = load_images(input_dir)

    user_content = []
    if images:
        user_content.extend(images)
    user_content.append({
        "type": "text",
        "text": (
            "## F&B 콘텐츠 가이드\n\n"
            f"{guide_text}\n\n"
            "위 가이드와 첨부된 음식/매장 이미지를 분석하여 콘텐츠를 작성해주세요. "
            "이미지에서 음식의 색감, 플레이팅, 식감 단서, 매장 분위기 등을 최대한 파악하여 반영해주세요."
        ),
    })

    agents = [
        ("블로그_네이버", BLOG_AGENT_PROMPT),
        ("유튜브_스크립트", YOUTUBE_AGENT_PROMPT),
        ("인스타그램", INSTAGRAM_AGENT_PROMPT),
    ]

    tasks = [run_agent(name, prompt, user_content) for name, prompt in agents]
    results = await asyncio.gather(*tasks)

    output_dir.mkdir(parents=True, exist_ok=True)
    filenames = []
    for (name, _), result in zip(agents, results):
        filename = f"{name}.md"
        (output_dir / filename).write_text(result, encoding="utf-8")
        filenames.append(filename)
        print(f"  저장: {output_dir / filename}")

    summary = (
        f"# F&B 파이프라인 실행 요약\n\n"
        f"- 실행 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"- 입력 이미지: {len(images)}장\n"
        f"- 생성 파일: {', '.join(filenames)}\n"
        f"- 모델: {MODEL}\n"
    )
    (output_dir / "pipeline_summary.md").write_text(summary, encoding="utf-8")

    print(f"\n{'=' * 60}")
    print(f"  완료! 산출물 -> {output_dir}")
    print(f"{'=' * 60}")
