from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import Alumnat  # Import your database connection file
import alumne, aula    # Import your schema file for Alumne
from models import Alumne
app = FastAPI()

# Pydantic model for Alumne
class Alumne(BaseModel):
    IdAlumne: int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    CreatedAt: str
    UpdatedAt: str

@app.get("/")
def read_root():
    return {"message": "Alumnat API"}

@app.get("/alumnes", response_model=List[dict])
def read_alumnes():
    db_data = Alumnat.read()  # Call to database function to read all alumnes
    return alumne.alumnes_schema(db_data)  # Convert the raw data to schema

@app.get("/alumnes/{id}", response_model=Alumne)
def read_alumne_id(id: int):
    alumne_data = Alumnat.read_id(id)  # Fetch alumne by ID
    if alumne_data is None:
        raise HTTPException(status_code=404, detail="Alumne not found")
    return alumne.alumne_schema(alumne_data)  # Convert to schema

@app.post("/alumne/add")
def add_alumne(alumne: Alumne):
    # check if IdAula exists in Aula table
    if not Alumnat.validate_id_aula(alumne.IdAula):
        raise HTTPException(status_code=400, detail="IdAula does not exist in Aula table")

    # Add the new alumne
    Alumnat.add_alumne(alumne)
    return {"message": "S'ha afegit correctament"}
@app.put("/alumne/update/{id}")
def update_alumne(id: int, alumne: Alumne):
    # Check if the alumne exists
    existing_alumne = Alumnat.read_id(id)
    if existing_alumne is None:
        raise HTTPException(status_code=404, detail="Alumne not found")
    
    # Validate IdAula if it's being updated
    if alumne.IdAula != existing_alumne[1]:  # Assuming the IdAula is at index 1
        if not Alumnat.validate_id_aula(alumne.IdAula):
            raise HTTPException(status_code=400, detail="IdAula does not exist in Aula table")

    # Update the alumne in the database
    Alumnat.update_alumne(
        id,
        alumne.IdAlumne,
        alumne.IdAula,
        alumne.NomAlumne,
        alumne.Cicle,
        alumne.Curs,
        alumne.Grup
    )
    return {"message": "S'ha modificat correctament"}

#to get aules
@app.get("/aules", response_model=List[dict])
def read_aules():
    db_data = aula.read_aules()
    return aula.aulas_schema(db_data)

