from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-120b")

message = [
    SystemMessage(content = "You are an helpful AI Assistant"),
    HumanMessage(content = "Explain me Langchain")
]
result = model.invoke(message)
message.append(AIMessage(content = result.content))
print(message)