import json
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

def main():
    with open("data/runbooks.json", "r") as f:
        runbooks = json.load(f)

    docs = [
        Document(
            page_content=f"{rb.get('symptom', '')}\n\n{rb.get('resolution', '')}",
            metadata=rb
        )
        for rb in runbooks
    ]

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local("incident_index")

    print(f"✅ Embedded {len(docs)} runbooks into FAISS and saved to incident_index")

if __name__ == "__main__":
    main()
