import streamlit as st
from flask import Flask, request, jsonify
from model import deepseek_chat
from summarizer import summarize_file
import os
import threading

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = deepseek_chat(data['message'])
    return jsonify({"response": response})

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    summary = summarize_file(file_path)
    return jsonify({"summary": summary})

def start_flask():
    app.run(host="0.0.0.0", port=5000)

def streamlit_ui():
    st.set_page_config(page_title="ChatBot DeepSeek R-1", layout="centered")

    st.title("🤖 ChatBot DeepSeek R-1")
    
    with st.form("chat_form"):
        user_input = st.text_input("Escribe tu mensaje:")
        submit_button = st.form_submit_button("Enviar")
        
        if submit_button and user_input:
            response = deepseek_chat(user_input)
            st.write("**Chatbot:**", response)

    uploaded_file = st.file_uploader("Sube un archivo para resumir:")
    if uploaded_file:
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        summary = summarize_file(file_path)
        st.success("Resumen generado:")
        st.text(summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)