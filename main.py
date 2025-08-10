from fastapi import FastAPI
import random 
from fastapi.responses import HTMLResponse


app= FastAPI(title="Random Number Generator", version="1.0.0")


@app.get("/", response_class=HTMLResponse)
async def root():
    # Return the HTML content above
    with open("index.html", "r") as f:
        return f.read()
@app.get("/random")
def random_no():
    return{"number": random.randint(1, 100)}

@app.get("/hi")
def hi():
    return{"hi Dhananjay this side !"}


