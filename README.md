This is a Streamlit application that creates a simple chat interface with a built-in language model (LLM) called Ollama. The app allows users to input a question, and the LLM responds with an answer.

Here's a breakdown of the code:

Importing Libraries

import streamlit as st
from langchain_ollama import ChatOllama

The code imports two libraries: streamlit (a Python library for building web applications) and ChatOllama from the langchain_ollama package (an LLM-based chat interface).

Setting Up the App

# Create your Title on the chat window
st.title("🔵💬Trợ lý ảo riêng cho gia đình!")

st.write('Tạo trợ lý ảo của riêng bạn đảm bảo tính bảo mật bằng sử dụng trong máy tính của bạn')

The app sets a title and displays a brief introduction to the chat interface.

Creating a Form

with st.form('llm-form'):
    text = st.text_area("Nhập câu hỏi của bạn, trợ lý ảo sẽ hỗ trợ ngay!")
    submit = st.form_submit_button("Submit")

This code creates a form with a text area for the user to input their question. When the "Submit" button is clicked, the form data will be sent to the generate_response function.

Generating Response

def generate_response(input_text):
    model = ChatOllama(model ='llama3.2:3b', base_url ="http://localhost:11434")

    response = model.invoke(input_text)

    return response.content

This is a custom function that takes the user's input text and uses it to interact with the Ollama LLM. The ChatOllama class is instantiated with specific parameters, and then the invoke method is called with the input text. The response from the LLM is returned as content.

Saving Chat History

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

This code checks if a session state key called chat_history exists. If it doesn't, it creates an empty list to store the chat history.

Generating Output and Saving Chat History

if submit and text:
    with st.spinner("⏳ Đang tìm câu trả lời..."):
        response = generate_response(text)
        st.session_state['chat_history'].append({'user': text, 'ollama': response})
        st.write(response)

When the "Submit" button is clicked, this code:

Calls the generate_response function to get the LLM's response.
Saves the chat history by appending a new dictionary with the user's input and the LLM's response.
Displays the response from the LLM.
Displaying Chat History

st.write('## 📜 Lịch sử các câu hỏi và câu trả lời')
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**🧑‍💻Hanu**: {chat['user']}")
    st.write(f"**💬Trợ lý ảo**: {chat['ollama']}")
    st.write("---")

This code displays the chat history by iterating over the chat_history list in reverse order. Each iteration writes the user's input and the LLM's response, followed by a separator line.

Overall, this code creates a simple chat interface with an LLM that responds to user input. The app saves the chat history for future reference.
