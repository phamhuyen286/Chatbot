import streamlit as st
from langchain_ollama import ChatOllama
#pip install -qU langchain-ollama
#pip install langchain

#Create your Title on the chat window
st.title("🔵💬Trợ lý ảo riêng cho gia đình!")

st.write('Tạo trợ lý ảo của riêng bạn đảm bảo tính bảo mật bằng sử dụng trong máy tính của bạn')

#Create a form where you want to interface with chatbot
with st.form('llm-form'):
    text = st.text_area("Nhập câu hỏi của bạn, trợ lý ảo sẽ hỗ trợ ngay!")
    submit = st.form_submit_button("Submit")
#create input chat from user
def generate_response(input_text):
    model = ChatOllama(model ='llama3.2:3b', base_url ="http://localhost:11434")

    response = model.invoke(input_text)

    return response.content
#save your chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
#generate your output
if submit and text:
    with st.spinner("⏳ Đang tìm câu trả lời..."):
        response = generate_response(text)
        st.session_state['chat_history'].append({'user': text, 'ollama': response})
        st.write(response)
st.write('## 📜 Lịch sử các câu hỏi và câu trả lời')
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**🧑‍💻Hanu**: {chat['user']}")
    st.write(f"**💬Trợ lý ảo**: {chat['ollama']}")
    st.write("---")
