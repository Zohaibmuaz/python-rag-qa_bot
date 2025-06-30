import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain import hub
from dotenv import load_dotenv
import tempfile

# --- SETUP ---
load_dotenv()

# --- GLOBAL ---
if "retrieval_chain" not in st.session_state:
    st.session_state.retrieval_chain = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- CORE LOGIC ---

def create_rag_chain(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splited_docs = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=splited_docs,
        embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    )

    retriever = vectorstore.as_retriever()
    rag_qa_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    llm = ChatOpenAI(temperature=0.7)
    combine_docs_chain = create_stuff_documents_chain(llm, rag_qa_prompt)

    chain = create_retrieval_chain(retriever, combine_docs_chain)
    return chain

def process_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    return create_rag_chain(tmp_path)

def handle_chat(user_input):
    if st.session_state.retrieval_chain is None:
        return "⚠️ Please upload a PDF file first."

    response = st.session_state.retrieval_chain.invoke({"input": user_input})
    return response["answer"]

# --- STREAMLIT UI ---

st.set_page_config(page_title="Chat with any PDF", layout="wide")

# Small red credit text
st.markdown(
    "<p style='color: red; font-size: 16px;'>Created by Zohaib Muaz</p>",
    unsafe_allow_html=True
)

# Main title
st.title("📄 Chat with any PDF")
st.write("Upload a PDF document and ask any question. The system will retrieve relevant content and answer you intelligently.")

# Upload Section
with st.sidebar:
    st.header("📁 Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file:
        st.session_state.retrieval_chain = process_pdf(uploaded_file)
        st.success(f"✅ Successfully processed '{uploaded_file.name}'")

# Chat Section
st.subheader("💬 Ask Questions")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question:")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        bot_reply = handle_chat(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_reply))

# Display Chat History
if st.session_state.chat_history:
    st.markdown("### 🧠 Chat History")
    for role, message in reversed(st.session_state.chat_history):
        with st.chat_message(role):
            st.markdown(message)
