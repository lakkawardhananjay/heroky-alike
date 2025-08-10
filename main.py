from fastapi import FastAPI
import random
app= FastAPI()


@app.get("/")
def read_root():
    return {"message":"🚀 Hello from FastAPI on Kubernetes with ArgoCD!"}
@app.get("/random")
def random_no():
    return{"number": random.randint(1, 100)}
