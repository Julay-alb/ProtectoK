from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector



foroRouter =  APIRouter()

class foroDB(BaseModel):
    nombre_foro: str
    descripcion_foro: str
    respuesta_foro: int

@foroRouter.get("/kutsadb_foro/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'Select * from foro'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@foroRouter.get("/kutsadb_foro/{foro_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(foro_id: int):
    select_query = "SELECT * FROM foro WHERE id_foro = %s"
    cleverCursor.execute(select_query, (foro_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Foro no encontrado")
    
@foroRouter.post("/kutsadb_crea_foro/", status_code=status.HTTP_201_CREATED)
def insert_user(foroPost: foroDB):
    insert_query = """
    INSERT INTO foro (nombre_foro, descripcion_foro, respuesta_foro)
    VALUES (%s, %s, %s)
    """
    values = (foroPost.nombre_foro, foroPost.descripcion_foro, foroPost.respuesta_foro)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysqlConn.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}
