# blog-pipeline — F&B 콘텐츠 멀티채널 발행 파이프라인

> 위치: `C:\Users\manid\blog-pipeline\`

매장/음식 **이미지와 가이드 텍스트** 를 입력으로 받아 **블로그(네이버)·유튜브 스크립트·인스타그램** 3채널 콘텐츠 초안을 병렬 생성하는 비동기 파이프라인.

---

## 파이프라인 구조

```
inputs/yyyymmdd_{이름}/
├── *.png / *.jpg / *.jpeg / *.gif / *.webp     (음식·매장 이미지)
└── guide.txt (또는 가이드.txt / 기타 .txt)      (콘텐츠 가이드)

         │
         ▼
  run_pipeline.py
         │
         ├── load_guide()      가이드 텍스트 로드
         ├── load_images()     이미지 리사이즈(1024px) + base64 인코딩, 최대 20장 균등 샘플링
         └── 3개 에이전트 병렬 실행 (asyncio.gather)
                ├── 블로그_네이버      (BLOG_AGENT_PROMPT)
                ├── 유튜브_스크립트     (YOUTUBE_AGENT_PROMPT)
                └── 인스타그램         (INSTAGRAM_AGENT_PROMPT)

outputs/yyyymmdd_{이름}/
├── 블로그_네이버.md
├── 유튜브_스크립트.md
├── 인스타그램.md
└── pipeline_summary.md
```

| 항목 | 값 |
|---|---|
| 모델 | `claude-sonnet-4-6` |
| 최대 이미지 수 | 20장 (초과 시 균등 샘플링) |
| 이미지 리사이즈 | 최대 1024px, JPEG/PNG |
| 동시성 | `asyncio.AsyncAnthropic` + `asyncio.gather` |

---

## 실행

```bash
cd blog-pipeline
pip install -r requirements.txt    # anthropic, python-dotenv, Pillow
cp .env.example .env               # ANTHROPIC_API_KEY 설정

# 최신 폴더만 처리 (Enter)
python run_pipeline.py

# 특정 폴더 지정
python run_pipeline.py 20260513_한입_비프파_넛츠_제품리뷰

# 전체 폴더 일괄 처리
python run_pipeline.py
# → 프롬프트에서 'a' 입력
```

---

## 입력 폴더 규칙

- 네이밍: `yyyymmdd_{매장명 또는 제품명}`
- 가이드 우선순위: `guide.txt` → `가이드.txt` → `*.txt` 첫 번째 매칭
- 이미지 확장자: `.png .jpg .jpeg .gif .webp`

---

## 프롬프트 정의

`prompts.py` 내 3개 상수:

| 상수 | 채널 | 톤·길이 |
|---|---|---|
| `BLOG_AGENT_PROMPT` | 네이버 블로그 | SEO 친화, 길이 풍부 |
| `YOUTUBE_AGENT_PROMPT` | 유튜브 쇼츠/롱폼 | 스크립트 형식 |
| `INSTAGRAM_AGENT_PROMPT` | 인스타 피드/릴스 | 캡션 중심, 짧고 임팩트 |

각 프롬프트는 이미지 분석(색감/플레이팅/식감 단서/매장 분위기) 결과를 반영하도록 지시됨.

---

## 관련 프로젝트

- `content-project/` — IT 취업 콘텐츠 4-에이전트 시퀀셜 파이프라인 (텍스트만)
- `likelion-owned-media/` — 발행 정책·SEO 가이드 정의
