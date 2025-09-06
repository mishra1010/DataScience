import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

# def create_embedding(): ---- we need to create embeddings by passing a list and so, we will use another way from ollama
#     r=requests.post("http://localhost:11434/api/embeddings", json={
#         "model": "bge-m3",
#         #"prompt": "Deep is a good boy"
#         "prompt": text
#     })
    #print(r.json())

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embeddings", json={
        "model": "bge-m3",
        #"prompt": "Deep is a good boy"
        "input": text_list
    })

    embedding = r.json()['embedding']
    return embedding
#    print(embedding[0:5])   # Print first 5 dimensions of the embedding

jsons = os.listdir("jsons")
# print(jsons)
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i, chunk in content['chunks']:
        chunk['chunk_id'] = chunk_id
       # chunk['embedding'] = create_embedding() - we do not want to use this as it was really slow to create embedding one by one for each text,
       #  so we created embeddings by passing a list as shown above
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        print(chunk)
        my_dicts.append(chunk)
    break  # remove this break to process all files
print(my_dicts)


df = pd.Dataframe.from_records(my_dicts)
print(df)

#save the dataframe
joblib.dump(df, "embeddings.joblib")
# a = create_embedding("Cat sad on the wall")

# print(a)
