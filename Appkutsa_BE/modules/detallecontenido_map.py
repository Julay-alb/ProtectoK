from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import mysql.connector

detallecontenidoRouter = APIRouter() #Se crea un objeto de tipo APIRouter