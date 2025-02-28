from modules.rol_map import rolRouter
from modules.foro_map import foroRouter
from modules.categoria_map import categoriaRouter
from modules.cursos_map import cursosRouter


def include_routers(app):
    app.include_router(rolRouter)
    app.include_router(foroRouter)
    app.include_router(categoriaRouter)
    app.include_router(cursosRouter)
