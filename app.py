import streamlit as st
from qa_graph import qa_app

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

import os

# Debug prints (optional)
print("Lang Smith Tracing enabled:", os.getenv("LANGCHAIN_TRACING_V2"))
print("Project name:", os.getenv("LANGCHAIN_PROJECT"))


# Streamlit UI setup
st.set_page_config(page_title="IT Incident Dashboard", layout="wide")
st.title("🚨 Real-Time IT Incident Resolution Dashboard")

with st.form("qa_form"):
    question = st.text_input("Describe an alert or ask for a resolution")
    submitted = st.form_submit_button("Get Recommendation")

if submitted:
    if not question.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            try:
                # Invoke LangGraph workflow with LangSmith config
                result = qa_app.invoke(
                    {"question": question},
                    config={
                        "run_name": "incident_query",
                        "tags": ["streamlit", "dashboard"],
                        "run_type": "graph"
                    }
                )

                # Display answer
                answer = result.get("answer", "⚠️ No answer returned.")
                st.markdown(f"**Answer:** {answer}")

                # Display retrieved documents
                docs = result.get("docs", [])
                if docs:
                    st.subheader("📚 Retrieved Runbook Entries")
                    for i, doc in enumerate(docs):
                        st.markdown(f"**{i+1}.** {doc.page_content}")

            except Exception as e:
                st.error(f"❌ Error: {e}")
