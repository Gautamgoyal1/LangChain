from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)
result = llm.invoke("what is the capital of india")
print(result.content)