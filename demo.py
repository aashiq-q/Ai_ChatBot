import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=groq_api_key, model_name="llama-3.1-8b-instant")

query = "Hi, how are you?"

response = llm.invoke(query)

print(response.content)