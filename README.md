# Customer Support Multi-Agent RAG Application

This project is a **Customer Support Application** built using **LangFlow**, integrating multi-agent architecture and Retrieval-Augmented Generation (RAG) to provide accurate and context-aware responses to user queries.

## Features
- **File Upload for RAG**:
  - Upload files to embed their contents into a vector-enabled database (AstraDB).
  - Automatically process and store data for use in queries.
  
- **Multi-Agent Architecture**:
  - **ManagerAgent** coordinates tasks and delegates responsibilities to:
    - **FAQAgent** for answering frequently asked questions.
    - **OrderLookupAgent** for retrieving order and product details.
  
- **Vector Database**:
  - Uses **AstraDB** for storing and querying vectorized data.
  - Embedding powered by Nvidia's **NV-Embed-QA** model for semantic search.

- **Dynamic Prompt Injection**:
  - Parses retrieved data and injects it into prompts for the language model.

- **Streamlit-Based Front-End**:
  - Provides a user-friendly chat interface for interacting with the application.

## Tech Stack
- **LangFlow** for multi-agent RAG workflows.
- **AstraDB** for vector database and semantic search.
- **Streamlit** for the front-end interface.
- **Python** for API integration and flow logic.
- **Nvidia NV-Embed-QA** for embedding generation.

## How It Works
1. **File Upload**: Upload a file to populate the knowledge base using the RAG workflow.
2. **Ask a Question**: Enter a query in the chat interface.
3. **Agent Selection**: The **ManagerAgent** intelligently routes the query to the appropriate agent.
4. **Database Search**: Agents query the AstraDB vector store for relevant data.
5. **Response**: Results are processed and displayed in the chat interface.

## Setup Instructions
### Prerequisites
- Python 3.8+
- AstraDB account and API token
- `.env` file with the following:
  ```env
  APP_TOKEN=<Your AstraDB Application Token>

## Installation
- **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/qna-chatbot.git
   cd qna-chatbot
   ```

- **Install the required dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

- **Run the application**:
  ```bash
  streamlit run app.py
  ```

## File Structure
```bash
├── app.py               # Streamlit front-end for the chat interface
├── .env                 # Environment variables (not included in the repo)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── Other project files  # LangFlow configuration and workflow files
```

## Example Query
- Input: "What is the status of my order #1001?"
- Response: "Your order #1001 is being processed."

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.


