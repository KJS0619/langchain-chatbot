# 🤖 전산통계 Q&A 챗봇 (Streamlit + LangChain)

컴퓨터 과학과 통계학 관련 질문에 대해 **쉽고 정확하게 답변하는 AI 챗봇**입니다.  
Streamlit UI + LangChain + OpenAI 모델을 기반으로 제작되었습니다.

---

## 🚀 주요 기능

- 💬 채팅형 인터페이스 (Streamlit)
- 🧠 대화 히스토리 유지 (Context-aware)
- 📊 컴퓨터 과학 + 통계학 전문 답변
- 🧾 코드 및 예시 포함 설명
- 🔄 LangChain 기반 체인 구성

---

## 🛠️ 기술 스택

- **Frontend/UI**: Streamlit
- **LLM**: OpenAI (gpt-4o-mini)
- **Framework**: LangChain
- **환경 관리**: python-dotenv

---

## 📂 프로젝트 구조

```
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ 설치 및 실행 방법

### 1️⃣ 저장소 클론

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ 가상환경 생성 (선택)

```bash
python -m venv .venv
source .venv/bin/activate
.venv\Scripts\activate
```

### 3️⃣ 패키지 설치

```bash
pip install -r requirements.txt
```

### 4️⃣ 환경 변수 설정

```
OPENAI_API_KEY=your_openai_api_key
```

### 5️⃣ 실행

```bash
streamlit run app.py
```

---

## 💡 사용 방법

1. 웹 브라우저에서 실행
2. 질문 입력
3. AI 답변 확인

---

## 🧠 내부 동작 구조

```
User Input → Prompt → LLM → Parser → Output
```

---

## 📦 requirements.txt

```
streamlit
langchain
langchain-core
langchain-openai
python-dotenv
openai
```

---

## ⚠️ 주의사항

- API 사용 비용 발생 가능
- .env 파일은 업로드 금지

---

## 📜 라이선스

MIT License

![alt text](image.png)