from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature=0
)
# 1st Prompt -> Detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
# 2nd Prompt -> Summary
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()
chain = template1 |  model | parser | template2 | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)

# If we do this same work without Chain then

# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()
# model = ChatGroq(
#     model = "openai/gpt-oss-120b",
#     temperature=0
# )
# # 1st Prompt -> Detailed report
# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']
# )
# # 2nd Prompt -> Summary
# template2 = PromptTemplate(
#     template = 'Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# prompt1 = template1.invoke({'topic':'black hole'})
# result = model.invoke(prompt1)
# prompt2 = template2.invoke({'text':result.content})
# result1 = model.invoke(prompt2)
# print(result1.content)