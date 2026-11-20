from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #importar cors para aceptar peticiones de otros dominios
from routers import usuarios

app = FastAPI(
    title="Gastwall API",
    description="API para la gestión de finanzas personales",
    version="1.0.0"
)

#configuración cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #permitir cualquier origen (se restringe en producción)
    allow_credentials=True,
    allow_methods=["*"],  #permitir cualquier metodo, como post, get, patch, put, delete
    allow_headers=["*"]   #permitir cualquier header
)

app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])

@app.get("/")
def root():
    return {"message": "Bienvenido a Gastwall API"}