import streamlit as st

st.title("🤖 My 100% Free AI Chatbot")
st.write("Type a message below to chat with my creation!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    ai_reply = f"Hello! You said: '{prompt}'. This chatbot was built by a 12-year-old genius!"
    
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
