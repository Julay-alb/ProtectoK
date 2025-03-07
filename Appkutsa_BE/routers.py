from modules.rol_map import rolRouter
from modules.foro_map import foroRouter
from modules.categoria_map import categoriaRouter
from modules.cursos_map import cursosRouter
from modules.quiz_map import quizRouter
from modules.biblioteca_map import bibliotecaRouter
from modules.usuarios_map import usuarioRouter
from modules.modulos_map import modulosRouter


def include_routers(app):
    app.include_router(rolRouter)
    app.include_router(foroRouter)
    app.include_router(categoriaRouter)
    app.include_router(cursosRouter)
    app.include_router(quizRouter)
    app.include_router(bibliotecaRouter)
    app.include_router(usuarioRouter)
    app.include_router(modulosRouter)
