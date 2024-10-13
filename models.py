from pydantic import BaseModel

class Alumne(BaseModel):  
    IdAlumne: int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    CreatedAt: str
    UpdatedAt: str
