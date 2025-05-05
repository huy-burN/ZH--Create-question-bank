from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import Gemini

# Load and process the PDF using OCR
pdf_path = "benhtieuduong.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load_and_split()
# documents = [doc for doc in documents if doc.page_content.strip()]  # Filter out empty pages
# Split the text into manageable chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Create embeddings and store them in a vector database
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(texts, embeddings)
#he
# Initialize the Gemini modelsss
llm = Gemini(model="gemini-1")  # Replace with the correct Gemini model name

# Create a conversational retrieval chains  
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=vectorstore.as_retriever())

# Chatbot
print("Chatbot is ready! Type 'exit' to quit.")
chat_history = []
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    response = qa_chain({"question": query, "chat_history": chat_history})
    chat_history.append((query, response["answer"]))
    print(f"Bot: {response['answer']}")

# Save the chat history to a file
with open("chat_history.txt", "w") as f:
    for question, answer in chat_history:
        f.write(f"You: {question}\n")
        f.write(f"Bot: {answer}\n")