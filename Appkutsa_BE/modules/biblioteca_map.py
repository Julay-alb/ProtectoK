from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import mysql
from Clever_MySQL_conn import cleverCursor, mysqlConn

bibliotecaRouter = APIRouter() #Se crea un objeto de tipo APIRouter

class bibliotecaDB(BaseModel):
    Nombre_Biblioteca: str #Nombre_Categoria
    Contenido_Biblioteca: str
    descripcion_Biblioteca: str

@bibliotecaRouter.get("/kutsadb_Biblioteca/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM Biblioteca'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@bibliotecaRouter.get("/kutsadb_Biblioteca/{Biblioteca_id}", status_code=status.HTTP_200_OK) #Se crea una ruta para obtener una categoria por su id
def get_user_by_id(Biblioteca_id: int):
    select_query = "SELECT * FROM Biblioteca WHERE id_Biblioteca = %s"
    cleverCursor.execute(select_query, (Biblioteca_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Biblioteca no encontrada")


@bibliotecaRouter.post("/kutsadb_Biblioteca/", status_code=status.HTTP_201_CREATED) #Se crea una ruta para insertar una categoria
def insert_categoria(categoriaPost: bibliotecaDB):
    insert_query = """
    INSERT INTO Biblioteca (Nombre_Biblioteca, Contenido_Biblioteca, descripcion_Biblioteca)
    VALUES (%s, %s, %s)
    """
    values = (categoriaPost.Nombre_Biblioteca, categoriaPost.Contenido_Biblioteca, categoriaPost.descripcion_Biblioteca)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))