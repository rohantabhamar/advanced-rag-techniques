from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


loader = TextLoader("my_data.txt")

doc = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 50,
    
)

text_spliter = splitter.split_documents(doc)