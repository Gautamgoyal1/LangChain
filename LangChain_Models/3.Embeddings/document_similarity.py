from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------------
# 1. Create embedding model
# -----------------------------------

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------------
# 2. Documents
# -----------------------------------

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


# -----------------------------------
# 3. User query
# -----------------------------------

query = "tell me about bumrah"


# -----------------------------------
# 4. Convert documents into embeddings
# -----------------------------------

doc_embeddings = embedding.embed_documents(documents)


# -----------------------------------
# 5. Convert query into embedding
# -----------------------------------

query_embedding = embedding.embed_query(query)


# -----------------------------------
# 6. Calculate cosine similarity
# -----------------------------------

scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]


# -----------------------------------
# 7. Find the most similar document
# -----------------------------------

index, score = sorted(
    list(enumerate(scores)),
    key=lambda x: x[1]
)[-1]


# -----------------------------------
# 8. Print result
# -----------------------------------

print("Query:", query)
print("\nMost relevant document:")
print(documents[index])

print("\nSimilarity score:", score)