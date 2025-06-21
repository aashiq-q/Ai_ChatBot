import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    llm = ChatGroq(api_key = groq_api_key, model_name = "llama-3.1-8b-instant")
    memory = ConversationBufferMemory()
    st.session_state.conversation = ConversationChain(
        llm = llm,
        memory = memory,
        verbose = False
    )

st.title("ChatBot")

left,right = st.columns(2)

with left:
    query = st.text_input("Ask me anything", label_visibility="collapsed")

with right:
    if st.button("Submit", type="primary"):
        st.session_state.chat_history.append("User: " + query + "\n")
        st.session_state.chat_history.append("AI: " + st.session_state.conversation.run(query) + "\n\n")
        st.rerun()

for message in st.session_state.chat_history:
    st.markdown(message) 