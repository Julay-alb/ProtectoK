from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

cursosRouter = APIRouter() #Se crea un objeto de tipo APIRouter

class cursosDB(BaseModel):
    nombre_curso: str
    descripcion_durso: str
    contenido_curso: str

 

@cursosRouter.get("/kutsadb_cursos/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM cursos'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@cursosRouter.get("/kutsadb_cursos/{curso_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(curso_id: int):
    select_query = "SELECT * FROM cursos WHERE id_curso = %s"
    cleverCursor.execute(select_query, (curso_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
@cursosRouter.post("/kutsadb_cursos/", status_code=status.HTTP_201_CREATED)
def insert_curso(cursoPost: cursosDB):
    insert_query = """
    INSERT INTO Cursos (nombre_curso, descripcion_curso, contenido_curso)
    VALUES (%s, %s, %s)
    """
    values = (cursoPost.nombre_curso, cursoPost.descripcion_curso, cursoPost.contenido_curso)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:  # Corrige la excepción
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Curso insertado correctamente"}