# This will not work as groq supports structured output with pydantic . to use with_structured_output we require open ai api which works with it otherwise a tool to connect them
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from typing import TypedDict

# load_dotenv()

# model = ChatGroq(
#     model = "openai/gpt-oss-120b"
# )
# class Review(TypedDict):
#     summary:str
#     sentiment:str

# structured_model = model.with_structured_output(Review)
# result = structured_model.invoke(""" he hardware is great , but the software feels bloated. there are too many pre_installed apps that I can't remove. Also the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")
# print(result)
# print(result['summary'])
# print(result['sentiment'])

# Working way 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

class Review(BaseModel):
    summary: str = Field(description="A short summary of the review")
    sentiment: str = Field(description="The sentiment of the review")

structured_model = model.with_structured_output(
    Review,
    method="json_schema"
)

result = structured_model.invoke(
    """The hardware is great, but the software feels bloated.
    There are too many pre-installed apps that I can't remove.
    Also the UI looks outdated compared to other brands.
    Hoping for a software update to fix this."""
)

print(result)
print(result.summary)
print(result.sentiment)
