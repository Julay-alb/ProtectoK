from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn

quizRouter =  APIRouter()

class quizDB(BaseModel):
    nombre_Rol : str

@quizRouter.get("/kutsadb_quiz/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'Select * from quiz'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@quizRouter.get("/kutsadb_quiz/{Quiz_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(quiz_id: int):
    select_query = "SELECT * FROM quiz WHERE id_quiz = %s"
    cleverCursor.execute(select_query, (quiz_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="quiz no encontrado")
    
@quizRouter.post("/kutsadb_crea_quiz/", status_code=status.HTTP_201_CREATED)
def insert_user(quizPost: quizDB):
    insert_query = """
    INSERT INTO quiz (nombre_quiz, descripcion_quiz, calificacion_quiz, actividad_quiz)

    VALUES (%s, %s, %s, %s)
    """
    values = (quizPost.nombre_quiz, quizPost.descripcion_quiz, quizPost.calificacion_quiz, quizPost.actividad_quiz)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysqlConn.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}