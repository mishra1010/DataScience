import requests

def create_embedding():
    r=requests.post("http://localhost:11434/api/embeddings", json={
        "model": "bge-m3",
        #"prompt": "Deep is a good boy"
        "prompt": text
    })
    #print(r.json())

    embedding = r.json()['embedding']
    return embedding

#    print(embedding[0:5])   # Print first 5 dimensions of the embedding


a = create_embedding("Cat sad on the wall")

print(a)