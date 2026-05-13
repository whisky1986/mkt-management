# likelion-owned-media — Owned Media 전략 프로젝트

> 위치: `C:\Users\manid\likelion-owned-media\`

멋쟁이사자처럼 B2C 부트캠프 사업의 **Owned Media 전략 허브**. 코드 실행보다는 전략·정책·콘텐츠 문서를 관리하고, Claude 슬래시 커맨드로 작성·검토를 자동화한다.

---

## 컨텍스트

```
조직: 멋쟁이사자처럼 (Likelion)
팀: CDC Chapter (B.E팀 + C.D.E팀)
역할: HEAD급 마컴 리드
범위: SEO/AEO, 콘텐츠 전략, CRM 연계, 채널별 운영 정책
```

### 핵심 이해관계자

| 코드명 | 역할 | 협업 시 주의 |
|---|---|---|
| CMO (상우님) | 최종 승인권자, KPI 조율 | 복잡도 낮은 커뮤니케이션 선호 |
| AXP | 내부 개발 파트너 | 리소스 사전 협의 필수 |
| B.E팀 | 브랜드 실행, 콘텐츠 발행 | 강사 전문성 콘텐츠 담당 |
| C.D.E팀 | 퍼포먼스, CRM, 전환 최적화 | 수강생 후기·전환 콘텐츠 담당 |

---

## 폴더 구조

```
likelion-owned-media/
├── CLAUDE.md                       # Claude Code 협업 규칙
├── README.md
├── 00_overview/                    # 프로젝트 브리프, 이해관계자 맵
├── 01_strategy/
│   ├── owned-media-strategy.md     # 마스터 전략 문서
│   ├── kpi-framework.md
│   └── channel-policy/
│       ├── blog.md                 # Inblog 운영 정책
│       ├── youtube.md              # 보류
│       └── sns.md
├── 02_content/
│   ├── seo-aeo-guide.md
│   ├── content-calendar.md
│   └── drafts/                     # [채널]_[주제]_draft.md
├── 03_crm/                         # 퍼널 매핑, 자동화 시나리오
├── 04_research/                    # 경쟁사·유저 리서치 노트
├── 05_reports/                     # 월별 성과 리포트
├── scripts/                        # GA4/Notion/키워드 자동화
└── .claude/commands/               # 슬래시 커맨드 정의
```

---

## 슬래시 커맨드

| 커맨드 | 기능 | 출력 위치 |
|---|---|---|
| `/new-content` | 채널별(blog/youtube/threads/x) 초안 생성 | `02_content/drafts/` |
| `/seo-review` | SEO/AEO 개선 포인트 점검 (표 출력) | 인라인 |
| `/weekly-report` | GA4 기반 주간 성과 요약 | `05_reports/` |
| `/script-gen` | 자동화 스크립트 생성 (GA4/Notion/키워드) | `scripts/` |
| `/strategy-review` | 전략 문서 자체 검토 | 인라인 피드백 |

---

## 작업 원칙

- **출력 형식**: Markdown 기본, 표 > 목록 > 서술형
- `.docx` / `.pptx` / `.xlsx` 생성 금지 (명시 요청 시만)
- 파일 네이밍: kebab-case (`owned-media-strategy.md`), 리포트는 `YYYY-MM_title.md`
- 항상 **복수 대안** 제시 — 단일 솔루션 금지
- 불확실성은 솔직하게 명시 (추정 vs 사실 구분)

---

## 현재 우선순위 (2026 Q1)

| 순위 | 과제 | 담당 |
|---|---|---|
| 🔴 1 | Inblog SEO 세팅 (`blog.likelion.co.kr`) | B.E |
| 🔴 2 | 콘텐츠 전략 이원화 (강사 전문성 vs 수강생 후기) | B.E |
| 🟡 3 | 오가닉 트래픽 기준선 재설정 (~19,500/월) | C.D.E |
| 🟡 4 | Initiative 3 검색광고 → AXP 핸드오프 | C.D.E |
| ⚪ 5 | YouTube 채널 전략 (보류) | — |

---

## 용어

| 용어 | 설명 |
|---|---|
| CDC Chapter | Content & Data Chapter (B.E + C.D.E 통합) |
| AEO | Answer Engine Optimization |
| Inblog | SEO 특화 블로그 (`blog.likelion.co.kr`) |
| CCC | 핵심 전환 비용 목표 (₩1,952,242) |
| 오가닉 기준선 | ~19,500/월 |
