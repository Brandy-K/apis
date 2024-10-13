from typing import List
from pydantic import BaseModel
import Alumnat  # Import your database functions
from fastapi import FastAPI, HTTPException
# Pydantic model for Aula
class Aula(BaseModel):
    IdAula: int
    DescAula: str
    Edifici: str
    Pis: str
def aula_schema(aula) -> dict:
    return {
        "IdAula": aula[0],
        "DescAula": aula[1],
        "Edifici": aula[2],
        "Pis": aula[3],
    }

def aulas_schema(aules) -> List[dict]:
    return [aula_schema(aula) for aula in aules]

# Function to get all Aula records
def read_aules():
    try:
        conn = Alumnat.db_client() 
        cur = conn.cursor()
        cur.execute("SELECT * FROM aula")  
        aules = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Connection error: {e}"}
    finally:
        conn.close()

    return aules

