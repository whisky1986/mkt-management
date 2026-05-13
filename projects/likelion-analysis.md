# likelion-analysis — KDT 유저/모객 데이터 분석 노트북

> 위치: `C:\Users\manid\likelion-analysis\`

멋쟁이사자처럼 KDT 부트캠프 **유저 데이터/모객현황/설문 분석** 을 위한 Jupyter Notebook 모음.

---

## 노트북 구성

| 파일 | 용도 |
|---|---|
| `kdt 모객현황 데이터 추출.ipynb` | KDT 부트캠프 기수별 모객 현황 추출/정리 |
| `likelioncampus.ipynb` | 멋사 캠퍼스(오프라인) 운영 데이터 분석 |
| `likelionuseralnalysis.ipynb` | 유저 행동·세그먼트 분석 |
| `mutdae_survey.ipynb` | 멋대 설문(서베이) 응답 분석 |
| `user analysis.ipynb` | 통합 유저 분석 |
| `userdata_sorting.ipynb` | 유저 데이터 전처리·정렬 유틸 |
| `23012412user.xlsx` | 분석 원본 데이터(스냅샷) |

---

## 실행

별도 패키지 설치 없이 Anaconda 환경에서 실행. 의존성은 노트북 상단 셀의 `import` 문 기준.

```bash
cd likelion-analysis
jupyter notebook
```

> 주요 라이브러리: `pandas`, `numpy`, `matplotlib`, `seaborn`, `openpyxl`

---

## 분석 흐름

1. **추출** — `kdt 모객현황 데이터 추출.ipynb` 또는 `userdata_sorting.ipynb` 로 원본 정제
2. **분석** — `likelionuseralnalysis.ipynb` / `user analysis.ipynb` 로 세그먼트·전환 지표 계산
3. **설문** — `mutdae_survey.ipynb` 로 NPS·만족도·정성 응답 코딩
4. **리포트** — 결과는 별도 `likelion-owned-media/05_reports/` 로 정리하거나 Notion 페이지로 발행

---

## 관련 프로젝트

- `competitor-analysis/` — 경쟁사 정기 모니터링 (Playwright + LLM)
- `likelion-owned-media/` — 분석 결과를 콘텐츠/전략 문서로 가공
- `kdt_dashboard/` — Streamlit 대시보드 (모객현황 시각화)
