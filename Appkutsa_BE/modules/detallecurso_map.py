from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

detallecursoRouter =  APIRouter()

class detallecursoDB(BaseModel):
    nombre_curso: str