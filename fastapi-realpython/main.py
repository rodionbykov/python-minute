from fastapi import FastAPI, HTTPException
from mongita import MongitaClientDisk
from pydantic import BaseModel

class Animal(BaseModel):
    id: int
    kind: str
    name: str

app = FastAPI()

client = MongitaClientDisk()
db = client.db
animals = db.animals

# animals.insert_one({"id": 1, "kind": "Cat", "name": "Felix"})
# animals.insert_one({"id": 2, "kind": "Dog", "name": "Spike"})
# animals.insert_one({"id": 3, "kind": "Raccoon", "name": "Ralph"})

@app.get("/")
async def get_root():
    return {"message": "Hello, world!"}

@app.get("/animals")
async def get_animals():
    our_animals = animals.find({})
    return [
        {key:animal[key] for key in animal if key != "_id"}
        for animal in our_animals
    ]

@app.get("/animals/{animal_id}")
async def get_animal_by_id(animal_id: int):
    if animals.count_documents({"id": animal_id}) > 0:
        animal = animals.find_one({"id": animal_id})
        return {key:animal[key] for key in animal if key != "_id"}
    raise HTTPException(status_code=404, detail=f"No animal with id {animal_id}")

@app.post("/animals")
async def add_animal(new_animal: Animal):
    animals.insert_one(new_animal.dict())
    return new_animal
