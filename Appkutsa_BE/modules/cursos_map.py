from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector
from sqlmodel import SQLModel, Relationship, Field
from categoria_map import Categoria

cursosRouter = APIRouter() #Se crea un objeto de tipo APIRouter
class Cursos(SQLModel, table=True):
    id_Curso: int = Field(default=None, primary_key=True)
    Nombre_Curso: str
    Descripcion_Curso: str
    Contenido_Curso: str
    categorias: list["Categoria"] = Relationship(back_populates="cursos")


class cursosDB(BaseModel):
    Nombre_Curso: str
    Descripcion_Curso: str
    Contenido_Curso: str

 

@cursosRouter.get("/kutsadb_Cursos/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM Cursos'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@cursosRouter.get("/kutsadb_Cursos/{Curso_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(Curso_id: int):
    select_query = "SELECT * FROM Cursos WHERE id_Curso = %s"
    cleverCursor.execute(select_query, (Curso_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
@cursosRouter.post("/kutsadb_Cursos/", status_code=status.HTTP_201_CREATED)
def insert_curso(cursoPost: cursosDB):
    insert_query = """
    INSERT INTO Cursos (Nombre_Curso, Descripcion_Curso, Contenido_Curso)
    VALUES (%s, %s, %s)
    """
    values = (cursoPost.Nombre_Curso, cursoPost.Descripcion_Curso, cursoPost.Contenido_Curso)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:  # Corrige la excepción
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Curso insertado correctamente"}