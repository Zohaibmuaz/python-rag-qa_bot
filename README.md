<div align="center">

<h1 align="center">📄 Chat with any PDF 💬</h1>

<p align="center">
  An intelligent, interactive chat application built with Streamlit and LangChain that allows you to have conversations with your PDF documents.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/Made%20with-LangChain-black.svg" alt="LangChain">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>
</div>

---

### **Table of Contents**

-   [✨ About The Project](#-about-the-project)
-   [⚙️ How It Works](#️-how-it-works)
-   [🚀 Getting Started](#-getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [🤝 Contributing](#-contributing)
-   [📄 License](#-license)

---

## ✨ About The Project

This project provides a user-friendly web interface to "chat" with any PDF file. Instead of manually searching through dense documents, you can simply ask questions and receive accurate, contextually relevant answers. It leverages the power of Large Language Models (LLMs) combined with a Retrieval-Augmented Generation (RAG) pipeline to ground the model's responses in the document's actual content.

<br>

## ⚙️ How It Works

The application follows a robust RAG architecture to ensure high-quality responses:

1.  **📄 Document Ingestion**: A PDF is uploaded via the Streamlit UI. `PyPDFLoader` loads and extracts the text.
2.  **✂️ Text Segmentation**: The text is segmented into smaller, overlapping chunks using `RecursiveCharacterTextSplitter` for optimal processing.
3.  **🧠 Vector Embedding**: Each text chunk is converted into a semantic vector embedding using Hugging Face's `all-MiniLM-L6-v2` model.
4.  **💾 Vector Storage**: These embeddings are indexed and stored in a `Chroma` vector database, creating a searchable knowledge base.
5.  **🤝 Retrieval & Generation**: When a user asks a question, the system retrieves the most relevant chunks from ChromaDB and passes them, along with the query, to an OpenAI LLM, which then generates a context-aware answer.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed:

-   Python (version 3.8 or higher)
-   An active **OpenAI API Key**

### Installation

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # Create a virtual environment
    python -m venv venv

    # Activate it
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Required Packages**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set Up Your Environment File**
    -   Create a new file named `.env` in the root of your project directory.
    -   Add your OpenAI API key to this file:
        ```env
        OPENAI_API_KEY="sk-YourSecretKeyHere"
        ```

5.  **Run the Streamlit App**
    ```sh
    streamlit run app.py
    ```
    Your browser should automatically open to the application's interface.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
