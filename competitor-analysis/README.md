# competitor-analysis — KDT 경쟁사 모니터링 멀티에이전트 파이프라인

> 위치: `C:\Users\manid\competitor-analysis\`

멋쟁이사자처럼 KDT 부트캠프 **경쟁사 정기 모니터링** 을 위한 4-Phase 비동기 멀티에이전트 파이프라인. Playwright 스크래핑 → LLM 구조화/분석/인사이트 → Notion + Slack 발행까지 end-to-end.

---

## 파이프라인 구조

```
main.py
└── orchestrator.py (헤드 에이전트)
    ├── [Phase 1] researcher.py         Playwright 스크래핑 + LLM 구조화
    ├── [Phase 2] analyzer.py           경쟁 매핑 + 변경사항 분류
    ├── [Phase 3] insight_generator.py  전략 인사이트 (Opus + extended thinking)
    └── [Phase 4] documenter.py         Notion 페이지 생성 + Slack 알림
```

### 모델 전략

| 에이전트 | 모델 | 이유 |
|---|---|---|
| researcher | `claude-sonnet-4-6` | 구조화 추출, 비용 효율 |
| analyzer | `claude-sonnet-4-6` | 분류·매핑, 중간 복잡도 |
| insight_generator | `claude-opus-4-6` + thinking | 고차원 전략 추론 |
| documenter | `claude-sonnet-4-6` | 요약 문서 작성 |

### 모니터링 대상

- FastCampus Kernel
- Sparta NBCamp
- CodeIt Sprint

---

## 실행

```bash
cd competitor-analysis
pip install -r requirements.txt
playwright install chromium             # 브라우저 설치
cp .env.example .env                    # API 키 입력

python main.py
```

또는 Claude Code 슬래시 커맨드 `/경쟁사분석`.

---

## 환경 변수 (`.env`)

| 변수 | 필수 | 설명 |
|---|---|---|
| `ANTHROPIC_API_KEY` | ✅ | Anthropic API 키 |
| `NOTION_TOKEN` | Notion 사용 시 | Integration 토큰 |
| `NOTION_PARENT_PAGE_ID` | Notion 사용 시 | 결과 저장 페이지 ID |
| `SLACK_WEBHOOK_URL` | Webhook 방식 | Incoming Webhook URL |
| `SLACK_BOT_TOKEN` | Bot 방식 | Bot OAuth 토큰 |
| `SLACK_CHANNEL` | Bot 방식 | 채널명 (예: `#kdt-분석`) |

---

## 캐시 전략

```
data/cache/{competitor_key}.json
```

- 경쟁사별 마지막 조사 결과 저장
- 재실행 시 **변경분(delta)** 만 분석 단계로 진입 → 첫 실행 대비 비용·시간 절감
- 캐시 무효화는 해당 JSON 파일 삭제로 처리

---

## 디버그 산출물

| 파일 | 용도 |
|---|---|
| `debug_scrape.json` | Phase 1 스크래핑 원본(raw HTML 파싱 결과) |
| `debug_extract.json` | Phase 1 LLM 구조화 결과 |

문제 발생 시 `outputs/` 와 함께 위 디버그 파일을 확인.

---

## 관련 프로젝트

- `likelion-owned-media/04_research/competitor-analysis.md` — 정성 분석·전략 해석 결과 저장
- `pm-go-to-market:battlecard` skill — 본 파이프라인 산출물을 sales-ready 배틀카드로 변환
