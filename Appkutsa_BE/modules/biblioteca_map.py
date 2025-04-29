from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

bibliotecaRouter = APIRouter() #Se crea un objeto de tipo APIRouter

class bibliotecaDB(BaseModel):
    nombre_biblioteca: str #Nombre_Categoria
    contenido_biblioteca: str
    descripcion_biblioteca: str

@bibliotecaRouter.get("/kutsadb_biblioteca/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM biblioteca'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@bibliotecaRouter.get("/kutsadb_biblioteca/{biblioteca_id}", status_code=status.HTTP_200_OK) #Se crea una ruta para obtener una categoria por su id
def get_user_by_id(biblioteca_id: int):
    select_query = "SELECT * FROM Biblioteca WHERE id_Biblioteca = %s"
    cleverCursor.execute(select_query, (biblioteca_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Biblioteca no encontrada")


@bibliotecaRouter.post("/kutsadb_biblioteca/", status_code=status.HTTP_201_CREATED) #Se crea una ruta para insertar una categoria
def insert_categoria(categoriaPost: bibliotecaDB):
    insert_query = """
    INSERT INTO biblioteca (nombre_biblioteca, contenido_biblioteca, descripcion_biblioteca)
    VALUES (%s, %s, %s)
    """
    values = (categoriaPost.nombre_biblioteca, categoriaPost.contenido_biblioteca, categoriaPost.descripcion_biblioteca)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))