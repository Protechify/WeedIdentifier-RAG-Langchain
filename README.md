# 🌱 Farmer Weed Identifier

Farmer Weed Identifier is an AI-powered agricultural assistant that helps farmers identify weeds and learn about them using a comprehensive weed knowledge base. The system provides information such as scientific names, growth patterns, flower characteristics, life cycles, and weed management recommendations.

## Features

### Weed Identification

* Identify weeds using weed characteristics.
* Search weeds by flower color, growth pattern, lifecycle, and other attributes.
* Access detailed weed information instantly.

### AI-Powered Assistant

* Ask questions about weeds in natural language.
* Receive intelligent responses using Retrieval-Augmented Generation (RAG).
* Get farming recommendations and weed management suggestions.

### Knowledge Base Search

* Scientific name lookup.
* Common name lookup.
* Growth pattern analysis.
* Flower characteristic matching.
* Lifecycle identification.

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Framework

* LangChain
* OpenAI

### Vector Database

* ChromaDB / FAISS

### Data Processing

* Pandas
* NumPy

## Project Structure

```bash
Farmer-Weed-Identifier/
│
├── app.py
├── rag.py
├── data/
│   ├── weeds.csv
│   └── documents/
│
├── vectorstore/
│
├── requirements.txt
├── .env
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/farmer-weed-identifier.git
```

Navigate to the project folder:

```bash
cd farmer-weed-identifier
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

```bash
streamlit run app.py
```

The application will run on:

```bash
http://localhost:8501
```

## Example Questions

* What is Musk Thistle?
* Show weeds with purple flowers.
* What is the growth pattern of Canada Thistle?
* How can I control perennial weeds?
* What is the scientific name of Houndstongue?

## Future Enhancements

* Image-based weed identification
* Mobile application
* Multi-language support
* Regional weed databases
* Voice-based farmer assistant
* Offline support

## License

MIT License

## Author

Developed to support farmers with AI-powered weed identification and agricultural knowledge.
