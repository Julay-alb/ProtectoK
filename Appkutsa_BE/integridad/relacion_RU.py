from sqlmodel import Field, SQLModel, Relationship
from modules.rol_map import roles
from modules.usuarios_map import usuario

class roles (SQLModel, table=True):
    id_rol: int = Field(default=None, primary_key=True)
    nombre_rol: str
    descripcion_rol: str
    usuario: list["usuario"] = Relationship(back_populates="OWNER")

class usuario (SQLModel, table=True):
    id_usuario: int = Field(default=None, primary_key=True)
    nombre_usuario: str
    apellido_usuario: str
    correo_usuario: str
    contrasena_usuario: str
    cedula_usuario: str
    rol_id: int = Field(foreign_key="roles.id_rol")
    OWNER: "roles" = Relationship(back_populates="usuario")