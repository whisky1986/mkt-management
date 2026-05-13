import asyncio
import sys
from pathlib import Path

from pipeline import run_pipeline

INPUTS_ROOT = Path(__file__).parent / "inputs"
OUTPUTS_ROOT = Path(__file__).parent / "outputs"


def find_input_folders(root: Path) -> list[Path]:
    """yyyymmdd_{text} 패턴의 하위 폴더를 이름순 정렬하여 반환."""
    folders = sorted(
        [d for d in root.iterdir() if d.is_dir()],
        key=lambda d: d.name,
    )
    return folders


def main():
    if len(sys.argv) > 1:
        folder_name = sys.argv[1]
        input_dir = INPUTS_ROOT / folder_name
        if not input_dir.exists():
            print(f"폴더가 존재하지 않습니다: {input_dir}")
            sys.exit(1)
        targets = [input_dir]
    else:
        targets = find_input_folders(INPUTS_ROOT)
        if not targets:
            print(f"inputs/ 폴더에 하위 폴더가 없습니다. yyyymmdd_이름 형태로 폴더를 만들어주세요.")
            sys.exit(1)
        print(f"발견된 폴더 {len(targets)}개:")
        for i, t in enumerate(targets, 1):
            print(f"  {i}. {t.name}")
        print()
        choice = input("처리할 폴더 번호 (전체: a, 최신: Enter): ").strip()
        if choice == "a":
            pass
        elif choice == "":
            targets = [targets[-1]]
        else:
            try:
                targets = [targets[int(choice) - 1]]
            except (ValueError, IndexError):
                print("잘못된 입력입니다.")
                sys.exit(1)

    for input_dir in targets:
        output_dir = OUTPUTS_ROOT / input_dir.name
        asyncio.run(run_pipeline(input_dir, output_dir))


if __name__ == "__main__":
    main()
