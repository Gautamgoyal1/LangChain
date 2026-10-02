from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableParallel , RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature=0
)
prompt1 = PromptTemplate(
    template = 'Write a tweet on {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template = 'write a linkedin post on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1,model,parser),
    'linkedin' :RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])