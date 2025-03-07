from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

modulosRouter = APIRouter()

class moduloDB(BaseModel):
    nombre_modulo: str
    descripcion_modulo: str
    contenido_modulo: str

@modulosRouter.get("/kutsadb_modulos/", status_code=status.HTTP_302_FOUND)
async def get_modulos():
    selectAll_query = 'Select * from modulos'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@modulosRouter.get("/kutsadb_modulos/{modulo_id}", status_code=status.HTTP_200_OK)
def get_modulo_by_id(modulo_id: int):
    select_query = "SELECT * FROM modulos WHERE id_modulo = %s"
    cleverCursor.execute(select_query, (modulo_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Modulo no encontrado")

@modulosRouter.post("/kutsadb_crea_modulo/", status_code=status.HTTP_201_CREATED)
def insert_modulo(moduloPost: moduloDB):
    insert_query = """
    INSERT INTO modulos (nombre_modulo, descripcion_modulo, contenido_modulo)
    VALUES (%s, %s, %s)
    """
    values = (moduloPost.nombre_modulo, moduloPost.descripcion_modulo, moduloPost.contenido_modulo)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConnection.commit()
    except mysqlConnection.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Modulo inserted successfully"}