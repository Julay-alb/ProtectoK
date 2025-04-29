from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

usuarioRouter = APIRouter()

class usuarioDB(BaseModel):
    nombre_usuario: str
    apellido_usuario: str
    correo_usuario: str
    contraseña_usuario: str
    cedula_usuario: str

@usuarioRouter.get("/kutsadb_usuario/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'Select * from usuarios'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@usuarioRouter.get("/kutsadb_usuario/{usuario_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(usuario_id: int):
    select_query = "SELECT * FROM usuarios WHERE id_usuario = %s"
    cleverCursor.execute(select_query, (usuario_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
@usuarioRouter.post("/kutsadb_crea_usuario/", status_code=status.HTTP_201_CREATED)
def insert_user(usuarioPost: usuarioDB):
    insert_query = """
    INSERT INTO usuarios (nombre_usuario, apellido_usuario, correo_usuario, contraseña_usuario, cedula_usuario)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (usuarioPost.nombre_usuario, usuarioPost.apellido_usuario, usuarioPost.correo_usuario, usuarioPost.contraseña_usuario, usuarioPost.cedula_usuario)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysqlConn.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Usuario inserted successfully"}