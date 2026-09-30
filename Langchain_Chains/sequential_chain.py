from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables= {'topic'}
)
prompt2 = PromptTemplate(
    template='Write a 5 line summary on given text /n {text}',
    input_variables=['text']
)
model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature=0
)
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'unemployment in India'})
print(result)
chain.get_graph().print_ascii()