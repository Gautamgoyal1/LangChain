from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
load_dotenv()
model = ChatGroq( model = "openai/gpt-oss-120b")
message = [
    SystemMessage(content = "You are an Helpful  AI Assistant")
]
while True:
    user_input = input("You: ")
    message.append(HumanMessage(content = user_input))
    if user_input == "exit":
        break;
    result = model.invoke(message)
    message.append(AIMessage(content = result.content)) 
    print("AI:",result.content)
print(message)