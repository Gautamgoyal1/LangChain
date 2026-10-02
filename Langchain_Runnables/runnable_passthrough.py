from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = 'tell me a joke on {topic}',
    input_variables=['topic']
)
model = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature=0
)
prompt2 = PromptTemplate(
    template='Explain this joke - {text}',
    input_variables=['text']
)

parser = StrOutputParser()

joke_gen = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanantion':RunnableSequence(prompt2,model,parser)
})
final_chain = RunnableSequence(joke_gen,parallel_chain)
print(final_chain.invoke({'topic':'cricket'}))