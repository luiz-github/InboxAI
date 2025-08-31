from fastapi import FastAPI
from src.routers import metaIA_router, upload_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metaIA_router.router, prefix="/api")
app.include_router(upload_router.router, prefix="/api")
