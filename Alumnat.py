import mysql.connector
from fastapi import FastAPI, HTTPException

def db_client():
    try:
        dbname = "Alumnat"  
        user = "root"
        password = "password"
        host = "localhost"
        port = "3306"
        collation = "utf8mb4_general_ci"
        
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            collation=collation
        )
            
    except Exception as e:
        return {"status": -1, "message": f"Connection error: {e}"}

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM alumne")  # Adjust to your actual table name
        alumnes = cur.fetchall()
    except Exception as e:
        return {"status": -1, "message": f"Connection error: {e}"}
    finally:
        conn.close()
    
    return alumnes

def read_id(id: int):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM alumne WHERE IdAlumne = %s"  # Adjust to your actual column name
        value = (id,)
        cur.execute(query, value)
        alumne = cur.fetchone()
    except Exception as e:
        return {"status": -1, "message": f"Connection error: {e}"}
    finally:
        conn.close()
    
    return alumne

def add_alumne(IdAlumne: int, IdAula: int, NomAlumne: str, Cicle: str, Curs: str, Grup: str):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
            INSERT INTO alumne (IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())
        """
        values = (IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup)
        cur.execute(query, values)
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding alumne: {e}")
    finally:
        conn.close()