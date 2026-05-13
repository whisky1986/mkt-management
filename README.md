# mkt-management

마케팅 업무용 프로젝트 모음 — 멋쟁이사자처럼 KDT 부트캠프 사업 관련 AI 파이프라인·전략 문서·데이터 분석.

각 프로젝트는 자체 폴더 안에 `README.md` 가 들어있어 실행법·구조·모델 전략을 설명합니다.

---

## 프로젝트

| 폴더 | 분류 | 설명 |
|---|---|---|
| [`resume-pipeline/`](resume-pipeline/) | AI 파이프라인 | KDT 부트캠프 지원자 미래이력서 생성 (Sonnet+Opus, 4-Phase) |
| [`likelion-owned-media/`](likelion-owned-media/) | 전략·콘텐츠 허브 | 멋사 Owned Media 전략·SEO/AEO·CRM 문서와 슬래시 커맨드 |
| [`likelion-analysis/`](likelion-analysis/) | 데이터 분석 | KDT 모객·유저·설문 Jupyter Notebook (output 셀 클리어 상태) |
| [`blog-pipeline/`](blog-pipeline/) | AI 파이프라인 | F&B 이미지+가이드 → 블로그·유튜브·인스타 멀티채널 콘텐츠 |
| [`competitor-analysis/`](competitor-analysis/) | AI 파이프라인 | KDT 경쟁사 4-Phase 비동기 모니터링 (Playwright + Notion/Slack) |

---

## 푸시 정책 (public 레포)

본 레포는 public이라 아래 항목은 **모두 .gitignore로 차단**되어 있습니다:

- `.env` 등 모든 시크릿 파일
- `data/`, `outputs/`, `inputs/`, `cache/` (PII·실데이터·재현 가능 산출물)
- `*.xlsx`, `*.xls`, `*.csv`, `*.parquet` (실데이터 가능성)
- `__pycache__/`, `.venv/`, `.ipynb_checkpoints/` 등 빌드/캐시 산출물

각 프로젝트의 실데이터·결과물은 로컬 환경(`C:\Users\manid\{프로젝트}\`)에만 존재합니다.

---

## 로컬 전용 (레포 미포함)

| 경로 | 내용 |
|---|---|
| `C:\Users\manid\Documents\whisky\` | Obsidian Vault — 책 프로젝트(2026.10 출간 목표)·멋사 업무·아카이브 |
| `C:\Users\manid\content-project\` | IT 취업 콘텐츠 4-에이전트 시퀀셜 파이프라인 (별도 레포 검토 중) |
| `C:\Users\manid\supporters-design\` | 대외활동/서포터즈 5-Phase 인사이트 파이프라인 |
| `C:\Users\manid\kdt_dashboard\` | KDT 모객현황 Streamlit 대시보드 |

---

## 실행 (공통)

각 프로젝트는 독립적으로 동작합니다. 폴더 진입 후 README 참조:

```bash
cd {project}
pip install -r requirements.txt
cp .env.example .env       # API 키 등 입력 (각 README 참조)
python main.py             # 또는 프로젝트별 진입점
```

| 공통 의존성 | 비고 |
|---|---|
| Python | Anaconda 또는 3.11+ |
| `anthropic>=0.40.0` | 모든 AI 파이프라인 |
| `playwright` | competitor-analysis (`playwright install chromium`) |
| `weasyprint` + GTK | resume-pipeline (Windows: GTK 런타임 별도 설치) |

---

## 모델 전략 요약

| 프로젝트 | Sonnet 단계 | Opus 단계 |
|---|---|---|
| resume-pipeline | Extractor, Profiler | Resume Writer (+ extended thinking) |
| competitor-analysis | Researcher, Analyzer, Documenter | Insight Generator (+ extended thinking) |
| blog-pipeline | 3채널 병렬 (블로그·유튜브·인스타) | — |
| likelion-owned-media | 슬래시 커맨드 (모델 무관) | — |
| likelion-analysis | (코드 없음, Jupyter 노트북) | — |
