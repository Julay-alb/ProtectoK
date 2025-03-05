from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector
from sqlmodel import SQLModel, Field, Relationship


foroRouter =  APIRouter()

class ForoDB(BaseModel):
    Nombre_Foro: str
    Descripcion_Foro: str
    Respuesta_Foro: int

@foroRouter.get("/kutsadb_foro/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'Select * from foro'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@foroRouter.get("/kutsadb_foro/{Foro_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(Foro_id: int):
    select_query = "SELECT * FROM foro WHERE id_Foro = %s"
    cleverCursor.execute(select_query, (Foro_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Foro no encontrado")
    
@foroRouter.post("/kutsadb_crea_foro/", status_code=status.HTTP_201_CREATED)
def insert_user(foroPost: ForoDB):
    insert_query = """
    INSERT INTO foro (Nombre_Foro, Descripcion_Foro, Respuesta_Foro)
    VALUES (%s, %s, %s)
    """
    values = (foroPost.Nombre_Foro, foroPost.Descripcion_Foro, foroPost.Respuesta_Foro)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysqlConn.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}
