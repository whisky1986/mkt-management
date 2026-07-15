# /seo-review — SEO/AEO 검토

## 역할
지정한 MD 파일의 SEO/AEO 최적화 상태를 점검하고 개선안을 표로 출력한다.

## 참조 규약
점검 기준은 `C:\Users\manid\seo-management\05-audit\audit-checklist.md`(섹션 B 콘텐츠 SEO + C GEO/AEO)를 원본으로 한다. 채널별 세부 기준(오운드미디어 블로그 등)은 `C:\Users\manid\seo-management\04-channel-playbooks\`에서 해당 채널 문서를 함께 확인한다. 아래 실행 지시의 점검 항목은 그 기준의 요약이며, 항목이 갱신되면 이 파일이 아니라 `seo-management` 허브를 먼저 갱신한다.

## Claude Code 실행 지시

```
다음 파일을 SEO/AEO 관점에서 검토해줘: [파일 경로]

먼저 C:\Users\manid\seo-management\05-audit\audit-checklist.md 의 B(콘텐츠 SEO)·C(GEO/AEO) 섹션을 로드하고,
발행 채널이 명시되어 있으면 C:\Users\manid\seo-management\04-channel-playbooks\{채널}.md 도 함께 로드해서 기준에 반영해줘.

점검 항목을 아래 표 형식으로 출력해줘:

| 항목 | 현재 상태 | 문제점 | 개선 제안 | 우선순위 |
|---|---|---|---|---|

점검 항목:
1. 제목 (H1) - 키워드 포함 여부, 길이 (30~60자)
2. 메타디스크립션 - 존재 여부, 길이 (120~155자), 키워드 포함
3. H2/H3 구조 - 논리적 흐름, 키워드 자연 배치
4. 키워드 밀도 - 과최적화/과소 사용 여부
5. 내부 링크 기회 - 연결 가능한 기존 콘텐츠
6. AEO 요소 - 질문형 소제목, 구조화된 답변, FAQ 형식
7. 이미지 alt text 누락 여부
8. CTA 존재 여부 및 위치
```

## AEO 체크리스트 (Answer Engine Optimization)

- [ ] 검색 의도에 직접 답하는 첫 단락 존재
- [ ] "~란?", "~하는 방법", "~의 차이" 형식 소제목
- [ ] 표/목록 형태의 구조화된 정보
- [ ] 200단어 내외의 명확한 정의 단락
- [ ] FAQ 섹션 (선택)

> 상세 원칙: `C:\Users\manid\seo-management\03-geo-aeo\geo-aeo-guide.md`
