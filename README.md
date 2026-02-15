# RAG-Onboarding-Assistant-FastAPI

This is a small RAG (Retrieval-Augmented Generation) project built with FastAPI and ChromaDB.

Instead of letting an LLM answer freely, the system first searches a local HR policy document and then sends only the relevant sections to the model.

---

## What This Project Does

There’s a text file inside `docs/Dummy_Data.txt`.  
It contains a fictional company’s HR policy.

When the app runs for the first time:

- The file is read  
- ChromaDB converts the text into embeddings (vectors)  
- Those vectors are stored locally in a persistent database  

After that, whenever a user asks a question:

1. The question is converted into an embedding  
2. ChromaDB searches for the most similar stored vectors  
3. The closest matching chunks are retrieved  
4. Those chunks are sent to the LLM  
5. The LLM generates a response using only that retrieved content  

So the model answers from the stored policy — not from general knowledge.

---

## Screenshot

[![Homepage](https://github.com/user-attachments/assets/ea42ec19-3285-488f-a2cd-1ed785d90b80)](https://github.com/user-attachments/assets/ea42ec19-3285-488f-a2cd-1ed785d90b80)

Example query:
```
How many days do I get off in a week?
```

---

## Tech Stack

- FastAPI  
- Python  
- ChromaDB (persistent vector store + default embedding model)  
- Mistral LLM API  
- Jinja2  
- HTML/CSS  

---

## Project Structure

RAG-Onboarding-Assistant-FastAPI  
│  
├── app/  
│   ├── api.py  
│   ├── routes.py  
│   ├── vectordb.py  
│  
├── docs/  
│   ├── Dummy_Data.txt  
│  
├── templates/  
│   ├── index.html  
│  
├── chroma db/   ← (create this folder manually before running)  
│  
├── main.py  
├── requirements.txt  

---

## Running Locally

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Make sure you manually create this folder in the root directory:

```
chroma db
```

3. Create a `.env` file in the root directory:

```
MISTRAL_API_KEY=your_mistral_api_key
VECTOR_DB_NAME=4386ee7c-2ee8-4b36-bc1e-64997126f67e   # example
```

4. Run the project:

```
python main.py
```

On the first run, ChromaDB will create a unique folder inside `chroma db/`.

Example:

[![ChromaDB Folder](https://github.com/user-attachments/assets/64438e49-c49f-4ef9-ba03-f1679f6fe325)](https://github.com/user-attachments/assets/64438e49-c49f-4ef9-ba03-f1679f6fe325)

After running once, copy the generated folder name and set it as your `VECTOR_DB_NAME` inside the `.env` file.

