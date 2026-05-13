# resume-pipeline — 멋사 미래이력서 생성 파이프라인

> 위치: `C:\Users\manid\resume-pipeline\`

KDT 부트캠프 지원자의 자기소개서와 부트캠프 정보를 결합해 **미래이력서(MD + HTML)** 를 자동 생성하는 4-Phase 시퀀셜 파이프라인.

---

## 파이프라인 구조

```
Phase 1: Extractor (Sonnet)          — CSV/Excel 지원서 → 구조화 데이터 추출
Phase 2: Profiler (Sonnet)           — 지원자 유형 분류 + 역량 매핑
Phase 3: Resume Writer (Opus)        — 이력서 콘텐츠 생성 (extended thinking)
Phase 4: Future Resume Renderer      — MD + HTML 렌더링 (순수 함수)
```

| 모델 | 사용 단계 |
|---|---|
| `claude-sonnet-4-6` | Phase 1 (추출), Phase 2 (분류) |
| `claude-opus-4-6` + extended thinking | Phase 3 (이력서 생성) |

---

## 생성 대상 필터

| 조건 | 컬럼 | 값 |
|---|---|---|
| 지원 완료 | `지원상태` | `지원완료` |
| 검토 대기 | `합불상태` | `검토전` |

- 자소서 텍스트가 10자 이하인 행 제외
- 이미 생성된 지원자(`{이름}_미래이력서.md` 존재)는 재실행 시 자동 스킵

---

## 실행

```bash
cd resume-pipeline
pip install -r requirements.txt
cp .env.example .env                          # ANTHROPIC_API_KEY 설정
python main.py \
  --bootcamp "data/sample/kdt-cld-7th 부트캠프 커리큘럼 정보.md" \
  --applications "data/sample/kdt-cld-7th_지원서_2026_05_11_17_50_42.csv"
```

미래이력서 단독 재생성 (Phase 1~3 intermediate 산출물 활용):

```bash
python generate_future_resume.py              # 미생성 대상 자동 탐색
python generate_future_resume.py --names 홍길동
```

---

## 출력 구조

```
outputs/YYYY-MM-DD/
├── {이름}_미래이력서.md
├── {이름}_미래이력서.html
├── 미래이력서_활용가이드.txt
├── intermediate/
│   ├── {이름}_1_extracted.json
│   ├── {이름}_2_profile.json
│   └── {이름}_3_content.json
├── batch_summary.json
└── pipeline.log
```

---

## 지원자 유형별 템플릿

| 유형 | 템플릿 | 레이아웃 |
|---|---|---|
| career_changer (전직자) | `career_changer.html` | 2단 + 전환 하이라이트 |
| student (대학생) | `student.html` | 단일 컬럼, 프로젝트 강조 |
| experienced (경력자) | `experienced.html` | 2단, 기술스택 전면 |

---

## 브랜딩

- 로고: `assets/likelion_logo.png`
- 컬러: `#FF7816` (메인), `#333333` (보조)
- 폰트: Pretendard (`templates/fonts/`)

> WeasyPrint Windows 설치: GTK 런타임 필요 — https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows
