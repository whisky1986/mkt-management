# Scripts — 자동화 스크립트 디렉토리

> Owned Media 운영을 위한 자동화 스크립트 모음  
> 작성 기준: Python 3.10+

---

## 스크립트 목록

| 파일명 | 목적 | 입력 | 출력 | 상태 |
|---|---|---|---|---|
| (추가 예정) | — | — | — | — |

---

## 공통 실행 환경 세팅

```bash
# 가상환경 생성 (최초 1회)
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# 패키지 설치
pip install -r requirements.txt
```

---

## 스크립트 추가 시 규칙

1. 파일명: `[목적]-[대상].py` (kebab-case)
2. 파일 상단에 docstring 필수:
   ```python
   """
   목적: 
   입력: 
   출력: 
   실행: python [파일명].py
   작성: YYYY-MM
   """
   ```
3. 이 README의 목록에 추가 필수
