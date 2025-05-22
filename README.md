
# Chatbot Backend
> A modular backend system for creating intelligent chat applications powered by large language models (LLMs). Built with FastAPI and MongoDB, it emphasizes scalability, adaptability, and clean design for production-grade AI assistants.

Chatbot Backend is the core of a conversational AI system designed to be modular and easy to plug into any frontend. It supports multiple LLM providers and uses MongoDB to persist conversation history.


---

##  Features
- **Modular LLM Engine**: Seamless integration with OpenAI, Azure, LlamaCpp, and Vertex AI.
- **Persistent Conversation Memory**: Built-in support for MongoDB for storing chat history.
- **Tooling System**: Easily extend the chatbot's capabilities by registering new tools.
- **RAG Workflow**: Native support for Retrieval-Augmented Generation (RAG) using document ingestion and vector search.
- **Structured Logging**: Detailed logging across request handling and LLM interactions.
- **Robust Error Handling**: Custom exceptions and graceful degradation.
- **Test-First Architecture**: Supports unit testing and debugging workflows.
- **FastAPI Backend**: Asynchronous, auto-documented API.
- **Clean Project Layout**: Separation of concerns for scalability and maintainability.  
- **Built-in endpoints** for chatting and history management.

---

##  Tech Stack

- **Python 3.11+**
- **FastAPI** (Web framework)
- **MongoDB** (Chat history persistence)
- **Ollama** (Local LLM inference)
- **Uvicorn** (ASGI server)

---

##  Folder Structure
```bash
llm-chatbot-backend/
├── api/                   # FastAPI application and routes
├── cli.py                 # Command-line chatbot client
├── rag_cli.py             # RAG-based chatbot using documents
├── src/
│   ├── core/              # LLM runners, memory, and tools
│   ├── services/          # Logic and orchestration
│   ├── common/            # Utilities, configs, and logging
├── .env                   # Environment configuration
├── requirements.txt
└── README.md
```
## Installation


### 1. Clone the repository

```bash
git clone https://github.com/ashmita-web/llm-chatbot-backend.git
cd llm-chatbot-backend
```
### 2. Set up a virtual environment and install dependencies


```bash
uv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

uv pip install -r requirements.txt
```

### 3. Environment Setup

Create a .env file in the root with the following configuration:

```bash

# MODEL CONFIGURATION
MODEL_TYPE=LLAMA  # Options: OPENAI, LLAMA, AZUREOPENAI, VERTEX

# OpenAI Configuration
OPENAI_API_KEY=your_openai_key
BASE_MODEL_NAME=gpt-3.5-turbo

# Azure OpenAI (Optional)
AZURE_CHAT_MODEL_KEY=your_key
AZURE_CHAT_MODEL_ENDPOINT=https://your-endpoint
AZURE_CHAT_MODEL_DEPLOYMENT=deployment-id
AZURE_CHAT_MODEL_VERSION=2024-02-15-preview

# MongoDB Configuration
MONGO_URI=mongodb://localhost:27017/chatbot
MONGO_DATABASE=langchain_bot
MONGO_COLLECTION=chatbot

# Vector Store (for RAG)
VECTOR_DATABASE_TYPE=CHROMA
VECTOR_DATABASE_CHROMA_PATH=./chroma_db

# Embedding Config
EMBEDDING_TYPE=AZUREOPENAI
AZURE_EMBEDDING_MODEL_KEY=your_key
AZURE_EMBEDDING_MODEL_ENDPOINT=https://your-endpoint
AZURE_EMBEDDING_MODEL_DEPLOYMENT=embedding-id
AZURE_EMBEDDING_MODEL_VERSION=2024-02-15-preview

# Server Config
PORT=8080
HOST=0.0.0.0
LOG_LEVEL=INFO
```


### 4. Running the Server

Start the backend server:
```bash
python app.py
```
The API will be available at http://localhost:8080 <br>
OpenAPI docs: http://localhost:8080/docs <br>
Health check: http://localhost:8080/health <br>


![image](https://github.com/user-attachments/assets/92b3ec8b-dd43-4c4a-83cc-e1b851a2b721)


![image](https://github.com/user-attachments/assets/434caed9-eeab-4c64-aa6d-0d13fbf12bdd)


![image](https://github.com/user-attachments/assets/b62546cc-c368-4816-b05b-d3046cff8a89)


### 5. Using the CLI

This project includes multiple CLI tools for testing different features.

Basic chat

```bash
python cli.py
```

Specify model type
```bash
python cli.py --model LLAMA

```
RAG-based chat (Document QA)


```bash
python rag_cli.py --document ./docs/yourfile.pdf

```
Use specific conversation

```bash
python rag_cli.py --conversation-id my_session

```
### 6. Running Tests

You can run all test suites using:
```bash
pytest tests/

```
### 7. Future Improvements


-Dockerfile for containerized deployment <br>
-OAuth or API key-based authentication <br>
-Web UI for chat sessions <br>
-Advanced vector store backends (e.g., Pinecone, Weaviate)

### 8. Contributing & Support

For issues, improvements, or ideas, feel free to open an issue or create a pull request.
