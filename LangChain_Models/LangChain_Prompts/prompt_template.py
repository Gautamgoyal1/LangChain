from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(
    model = "openai/gpt-oss-120b"
)
template = PromptTemplate(
    template = "Greet this person in 5 languages. The name of the person is {name}",
    input_variables = {'name'}
)
prompt = template.invoke({'name':'Gautam'})
result = model.invoke(prompt)
print(result.content)