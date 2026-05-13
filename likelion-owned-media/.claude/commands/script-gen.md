# /script-gen — 자동화 스크립트 생성

## 역할
마케팅 자동화, 데이터 수집/정제, 리포트 생성 등을 위한 스크립트를 작성한다.

## Claude Code 실행 지시

```
다음 조건으로 자동화 스크립트를 작성해줘.

목적: [한 문장으로]
입력: [입력 데이터 형식 - CSV / GA4 API / Google Sheets 등]
출력: [원하는 결과물]
언어: Python (기본) / Shell / Apps Script
실행 환경: [Mac / 서버 / Google Apps Script]

파일명: [목적]-[대상].py
저장 위치: scripts/

포함 요소:
- 주석 (한국어, 각 섹션 설명)
- 에러 핸들링
- scripts/README.md 에 사용법 추가
```

## 자주 쓰는 스크립트 유형

| 유형 | 설명 | 예시 파일명 |
|---|---|---|
| GA4 데이터 추출 | API로 트래픽 지표 수집 | `fetch-ga4-metrics.py` |
| 콘텐츠 캘린더 동기화 | Notion ↔ 스프레드시트 | `sync-content-calendar.py` |
| SEO 순위 추적 | 키워드별 검색 순위 모니터링 | `track-keyword-rank.py` |
| 발행 체크리스트 | MD 파일 SEO 항목 자동 검사 | `check-seo-checklist.py` |
| CRM 태그 정제 | 빅인사이트/솔라피 데이터 전처리 | `clean-crm-tags.py` |
