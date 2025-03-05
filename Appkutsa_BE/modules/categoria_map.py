from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

categoriaRouter = APIRouter() #Se crea un objeto de tipo APIRouter

class categoriaDB(BaseModel):
    tipo_categoria: str #Nombre_Categoria

@categoriaRouter.get("/kutsadb_categoria/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM categoria'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@categoriaRouter.get("/kutsadb_categoria/{categoria_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(categoria_id: int):
    select_query = "SELECT * FROM categoria WHERE id_categoria = %s"
    cleverCursor.execute(select_query, (categoria_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    
@categoriaRouter.post("/kutsadb_categoria/", status_code=status.HTTP_201_CREATED)
def insert_categoria(categoriaPost: categoriaDB):
    insert_query = """
    INSERT INTO categoria (tipo_categoria)
    VALUES (%s)
    """
    values = (categoriaPost.tipo_categoria,)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:  # Corrige la excepción
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Categoria insertada correctamente"}


    
    