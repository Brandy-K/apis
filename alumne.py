from typing import List
def alumne_schema(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "CreatedAt": alumne[6],
        "UpdatedAt": alumne[7],
    }

def alumnes_schema(alumnes) -> List[dict]:
    return [alumne_schema(alumne) for alumne in alumnes]
