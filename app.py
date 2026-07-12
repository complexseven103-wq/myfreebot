import streamlit as st
import requests

st.title("🤖 My Smart AI Chatbot")
st.write("Ask me anything! Powered by a real AI brain.")

# Your secret Hugging Face token key is locked in below!
API_TOKEN = "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"

# This points to Mistral 7B, a super smart open-source AI brain
API_URL = "https://huggingface.com"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me a question..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call the real AI brain
    try:
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 250}}
        response = requests.post(API_URL, headers=headers, json=payload).json()
        ai_reply = response['generated_text'].replace(prompt, "").strip()
    except:
        ai_reply = "Oops! My AI brain is waking up. Try typing your message again in a few seconds!"
    
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
