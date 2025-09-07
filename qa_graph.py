from langgraph.graph import StateGraph
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from pydantic import BaseModel
from typing import List


# Define state schema
class QAState(BaseModel):
    question: str
    docs: List = []
    answer: str = ""

# Load retriever
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectordb = FAISS.load_local(
    "incident_index",
    embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectordb.as_retriever()

# Load LLM
llm = OllamaLLM(model="llama3.2:1b", base_url="http://localhost:11434")

# Define node functions
def retrieve_node(state: QAState):
    docs = retriever.get_relevant_documents(state.question)
    return {"docs": docs}

def answer_node(state: QAState):
    context = "\n\n".join([d.page_content for d in state.docs])
    prompt = f"Context:\n{context}\n\nQuestion: {state.question}\nAnswer:"
    answer = llm.invoke(prompt)
    return {"answer": answer}

# Build LangGraph workflow
graph = StateGraph(QAState)
graph.add_node("retrieve", retrieve_node)
graph.add_node("answer", answer_node)
graph.add_edge("retrieve", "answer")
graph.set_entry_point("retrieve")

qa_app = graph.compile()
