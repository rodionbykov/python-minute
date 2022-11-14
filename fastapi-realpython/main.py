from fastapi import FastAPI, HTTPException

app = FastAPI()

animals = [
    {"id": 1, "kind": "Cat", "name": "Felix"},
    {"id": 2, "kind": "Dog", "name": "Spike"},
    {"id": 3, "kind": "Raccoon", "name": "Ralph"}
]

@app.get("/")
async def get_root():
    return {"message": "Hello, world!"}


@app.get("/animals")
async def get_animals():
    return animals

@app.get("/animals/{animal_id}")
async def get_animal_by_id(animal_id: int):
    for animal in animals:
        if animal["id"] == animal_id:
            return animal
    raise HTTPException(status_code=404, detail=f"No animal with id {animal_id}")

