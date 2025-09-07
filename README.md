# IncidientIQDashboard-Langchain-Langgraph-Langsmith
Langchain-Langgraph-Langsmith

realtime-it-incident-dashboard/
├── data/
│   │   └── runbooks.json
├── build_graph.py
├── qa_chain.py
├── app.py
├── requirements.txt
🚀 IncidentIQ: AI-Powered Resolution Dashboard
 (Built with LangChain + LangGraph + LangSmith)

In IT operations, every second counts.
 That’s why I built an AI-driven dashboard that transforms alerts into answers — faster, smarter, and with complete visibility.

🌟 <<<Key Highlights>>>
🚨 Purpose-Driven Design
Built to assist IT teams in resolving incidents faster and more intelligently.
Translates natural language alerts into actionable recommendations.

🧠 Intelligent Retrieval
Uses FAISS to search embedded runbook entries based on semantic similarity.
Embeddings generated with Ollama’s nomic-embed-text model — fully offline.

🧩 Modular Workflow with LangGraph
Orchestrated using LangGraph’s StateGraph, enabling clean node-based logic.
Two core nodes: retrieve and answer, with shared state transitions.

🗂️ Structured Knowledge Base
Runbooks stored as JSON, embedded into a vector store.
Combines symptom and resolution fields for context-rich retrieval.

🧪 Local LLM Inference
Powered by Ollama’s llama3.2:1b model for generating responses.
No external API calls — fast, private, and customizable.

🧭 Full Observability with LangSmith
Every query is traced: input, retrieved docs, prompt, output.
Visual graph of LangGraph execution, token usage, and latency.
Tagged runs for filtering and evaluation (streamlit, dashboard, incident_query).

💻 Streamlit Dashboard
Clean UI for entering alerts and viewing recommendations.
Displays both the generated answer and the retrieved runbook entries.

This project combines the power of LangChain, LangGraph, and LangSmith into a single ecosystem — enabling IT teams to detect, diagnose, and resolve incidents like never before.
<<<@copyright Rathiga Ramesh 2025>>>


