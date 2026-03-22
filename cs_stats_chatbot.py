import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# 환경변수 로드
load_dotenv()

# 채팅 히스토리 초기화
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 컴퓨터 과학과 통계학 전문가야. 사용자의 질문에 대해 정확하고 이해하기 쉽게 한국어로 답변해. 예시나 코드를 포함해서 설명해."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])

# 모델 및 파서

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
parser = StrOutputParser()

# 체인 구성
chain = prompt | llm | parser

# Streamlit UI
st.title("전산통계 Q&A 챗봇 🤖")
st.write("컴퓨터 과학과 통계학 관련 질문을 입력하세요.")

# 채팅 히스토리 표시
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
user_input = st.chat_input("질문을 입력하세요...")

if user_input:
    # 사용자 메시지 추가
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 메시지 히스토리를 LangChain 형식으로 변환
    history_messages = []
    for msg in st.session_state.chat_history[:-1]:  # 마지막 사용자 입력은 제외
        if msg["role"] == "user":
            history_messages.append(HumanMessage(content=msg["content"]))
        else:
            history_messages.append(AIMessage(content=msg["content"]))

    # AI 응답 생성
    response = chain.invoke({"history": history_messages, "input": user_input})

    # AI 메시지 추가 및 표시
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)