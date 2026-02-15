# RAG-Onboarding-Assistant-FastAPI

A simple RAG-based onboarding assistant built using FastAPI and ChromaDB.

It answers questions using a stored HR policy document and a vector database.

---

## Homepage

[![Homepage](https://github.com/user-attachments/assets/ea42ec19-3285-488f-a2cd-1ed785d90b80)](https://github.com/user-attachments/assets/ea42ec19-3285-488f-a2cd-1ed785d90b80)

---

## How It Works

- `docs/Dummy_Data.txt` contains a dummy company HR policy.
- On first run, ChromaDB reads this file.
- ChromaDB uses its default embedding model to convert the text into vectors.
- These vectors are stored locally in a persistent database.

When a user enters a question:

1. The query is converted into a vector.
2. ChromaDB finds the most similar stored vectors.
3. The matching text chunks are retrieved.
4. These chunks are sent to the LLM.
5. The LLM generates a response based only on that retrieved text.

---

## Tech Stack

- FastAPI
- Python
- ChromaDB (persistent vector store)
- Jinja2
- Mistral LLM API
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
├── chroma db/  (must be created manually)  
├── main.py  
├── requirements.txt  

---

## Setup

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create an empty folder:

```
chroma db
```

3. Create `.env` file:

```
MISTRAL_API_KEY=your_mistral_api_key
VECTOR_DB_NAME=your_vector_folder_name
```

4. Run once to generate the vector folder:

```bash
python main.py
```

After the first run, ChromaDB will create a folder inside `chroma db/`.

Example:

[![ChromaDB Folder](https://github.com/user-attachments/assets/64438e49-c49f-4ef9-ba03-f1679f6fe325)](https://github.com/user-attachments/assets/64438e49-c49f-4ef9-ba03-f1679f6fe325)

Copy that folder name and set:

```
VECTOR_DB_NAME=a3e97df6-5e7c-4316-87f7-85931b144413
```

---

## Example Query

```
How many days do I get off in a week?
```
