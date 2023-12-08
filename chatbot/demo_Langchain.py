import streamlit as st
from Model_Langchian import agent_conversation_chain, agent_Format

if 'show_initial_message' not in st.session_state:
    st.session_state.show_initial_message = True

st.title('Chat with LLM')
user_input = st.text_input("You: ")

if st.button('Send'):
    text = user_input
    print(text)
    response = agent_conversation_chain(123, user_input)

    if response == 'It was great talking to you':
        st.write('LLM: ', response)
        genrated = agent_Format(text)

    st.write('LLM: ', response)

if st.session_state.show_initial_message:
    st.write('LLM: ', "Hello! How are you doing?")
    st.session_state.show_initial_message = False  # Set the flag to False after the initial message is shown
