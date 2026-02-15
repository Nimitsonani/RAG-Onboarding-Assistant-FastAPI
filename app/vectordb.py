import os

import chromadb
from pathlib import Path
from dotenv import load_dotenv

load_dotenv('.env')
vector_db_name = os.getenv('VECTOR_DB_NAME')

#create client and collection
client = chromadb.PersistentClient(path="chroma db/")
collection = client.get_or_create_collection(name="my-collection")

#create Vectors if doesnt exist
path = Path(f'chroma db/{vector_db_name}')
if path.exists():
    print('passes')
else:
    # load all vector lines into a list
    with open('docs/Dummy_Data.txt', encoding='utf-8') as f:
        vectors = f.read().splitlines()
    print(vectors)
    collection.add(
        ids=[str(i) for i in range(222)],
        documents=vectors
    )
    print('Vectors created.')

def query_db(query):
    result = collection.query(
        query_texts=[query],
        n_results=3
    )
    print(result)
    finale_op=[]
    for i in range(3):
        if result['distances'][0][i]<1.2:
            finale_op.append(result['documents'][0][i])

    return finale_op