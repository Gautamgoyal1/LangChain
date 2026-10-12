from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf') # typed a random file name if you have pdf write the name or path of that pdf file

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)