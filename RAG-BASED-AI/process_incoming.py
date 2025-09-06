import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from read_chunks import create_embedding
import numpy as np
import joblib
import requests

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embeddings", json={
        "model": "bge-m3",
        #"prompt": "Deep is a good boy"
        "input": text_list
    })
    embedding = r.json()['embedding']
    return embedding

df = joblib.load("embeddings.joblib")

incoming_query = input("Enter your query: ")
question_embedding = create_embedding([incoming_query])[0]
print(question_embedding)

# Find similarities of question_embedding with all the chunk embeddings
#print(np.vstack(df['embedding'].values)) # np.vstack converts the list of arrays into a 2D array
#print(df['embedding'].shape)
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten() # flatten converts 2D array to 1D array
#print(similarities)
top_results = 3
similarities.argsort()  # sorts the array and returns the indices of the sorted array

max_indx = similarities.argsort()[::-1][0:top_results]  # top 3 results
#print(max_indx)
new_df = df.loc[max_indx]
print(new_df[['title','number','text', 'similarities']])

for index, item in new_df.iterrows():
    print(index, item['title'], item['number'], item['text'], item['start'], item['end'])