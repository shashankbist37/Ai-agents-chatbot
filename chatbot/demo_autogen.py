import streamlit as st
from model_autogen import agent_conversation_chain,agent_Format
text=""

st.title('Chat with LLM')
user_input = st.text_input("You: ")
if st.button('Send'):
    text+=user_input
    response = agent_conversation_chain(123,user_input)
    if response=='It was a great to talk to you':
        st.write('LLM: ', response)
        genrated = agent_Format(text)   
    st.write('LLM: ', response)
    