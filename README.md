# 🗨️ Streamlit Chatbot using LangChain and Groq API

This project is a simple conversational AI **Chatbot** built with **Streamlit**, powered by **LangChain** and **Groq's Llama 3.1 model**. It supports ongoing conversation memory, so you can chat with it naturally, and all messages are displayed interactively on the web interface.

![Chatbot Screenshot](https://github.com/aashiq-q/Ai_ChatBot/blob/main/ChatBot_Image.png)


---

## ✨ **Features**

- ✅ Interactive web-based chatbot UI using Streamlit.
- ✅ Uses **LangChain**'s `ConversationChain` with a `ConversationBufferMemory` for context-aware conversations.
- ✅ Powered by **Groq Llama 3.1** for fast, high-quality responses.
- ✅ Easy to deploy locally.
- ✅ Secure API key management via `.env`.

---

## 📦 **Tech Stack**

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.dev/)
- [Groq Llama 3.1](https://groq.com/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ **Setup Instructions**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/aashiq-q/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a virtual environment (recommended)
```
# For Windows
python -m venv .venv
.venv\Scripts\activate
```
```
# For Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Configure your .env file
Create a .env file in your project root and add your Groq API key or Any other LLM API Key:
```
GROQ_API_KEY=your_groq_api_key_here 
```
or
```
OPENAI_API_KEY = your_openai_api_key_here
```
Important:
Add .env to your .gitignore to keep your API key secret.


### 5️⃣ Run the Streamlit app
```
streamlit run app.py
```

## 💡 How it works

- When you open the app, you can type any question into the input box.
- The conversation uses ConversationChain from LangChain to keep track of what you said previously.
- All messages are stored in st.session_state and displayed nicely in order.

### 🚫 .gitignore example
Make sure your .gitignore includes:
```
.env
.venv/
__pycache__/
```

## 📜 License
This project is for educational and personal use. Feel free to adapt and improve it!

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain) — Framework for building LLM-powered applications.
- [Groq](https://www.groq.com/) — High-performance LLM inference engine.
- [Streamlit](https://github.com/streamlit/streamlit) — Open-source Python library for building beautiful web apps.

