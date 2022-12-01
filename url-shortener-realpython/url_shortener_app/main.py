import validators

from fastapi import FastAPI, HTTPException

from . import schema

app = FastAPI()

@app.get("/")
def get_home():
    return "Hello world"

@app.post("/")
def create_url(url: schema.URLBase):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Invalid target URL provided")
    
    return "Here be code"
