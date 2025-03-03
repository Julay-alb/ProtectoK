from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import mysql
from Clever_MySQL_conn import cleverCursor, mysqlConn

categoriaRouter = APIRouter() #Se crea un objeto de tipo APIRouter

cleverCursor.execute("""
CREATE TABLE IF NOT EXISTS Categoria (
    id_Categoria INT AUTO_INCREMENT PRIMARY KEY,
    Tipo_Categoria VARCHAR(255),
    Cursos_id INT NOT NULL,
    Foro_id INT NOT NULL,
    FOREIGN KEY (Cursos_id) REFERENCES Cursos(id_Cursos),
    FOREIGN KEY (Foro_id) REFERENCES Foro(id_Foro)
)
""")

class categoriaDB(BaseModel):
    Tipo_Categoria: str #Nombre_Categoria

@categoriaRouter.get("/kutsadb_Categoria/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'SELECT * FROM Categoria'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@categoriaRouter.get("/kutsadb_Categoria/{Categoria_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(Categoria_id: int):
    select_query = "SELECT * FROM Categoria WHERE id_Categoria = %s"
    cleverCursor.execute(select_query, (Categoria_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    
@categoriaRouter.post("/kutsadb_Categoria/", status_code=status.HTTP_201_CREATED)
def insert_categoria(categoriaPost: categoriaDB):
    insert_query = """
    INSERT INTO categoria (Tipo_Categoria)
    VALUES (%s)
    """
    values = (categoriaPost.Tipo_Categoria,)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysql.connector.Error as err:  # Corrige la excepción
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "Categoria insertada correctamente"}


    
    