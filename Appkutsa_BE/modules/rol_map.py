from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn

rolRouter = APIRouter()

class rolDB(BaseModel):
    Nombre_Rol: str

@rolRouter.get("/kutsadb_roles/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM roles'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@rolRouter.get("/kutsadb_roles/{Rol_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(Rol_id: int):
    select_query = "SELECT * FROM roles WHERE id_Rol = %s"
    cleverCursor.execute(select_query, (Rol_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="rol no encontrado")

@rolRouter.post("/kutsadb_crea_roles/", status_code=status.HTTP_201_CREATED)
def insert_rol(rolesPost: rolDB):
    insert_query = """
    INSERT INTO roles (Nombre_Rol)
    VALUES (%s)
    """
    values = (rolesPost.Nombre_Rol,)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:  # Corrige la excepción
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Rol insertado correctamente"}


