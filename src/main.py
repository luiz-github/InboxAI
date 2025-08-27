from fastapi import FastAPI
from routers import openIA_router

app = FastAPI()

# Inclui as rotas definidas em routers/usuarios.py
app.include_router(openIA_router.router, prefix="/api")
