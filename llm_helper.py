from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="qwen/qwen3-32b")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are? Answer concisely, in one line. No thinking")
    print(response.content)




