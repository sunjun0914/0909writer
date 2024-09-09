

#from dotenv import load_dotenv
#load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

st.title('시인급 실력의 박선준이 써주는 시')

content = st.text_input('작사할 주제를 제시해주세요。')

if st.button('작사 요청하기'):
    result = chat_model.invoke(content + "에 대한 노래의 작사를 해 줘")
    st.write(result.content)