from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# Configuración para servir archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Lista de comentarios en memoria
comentarios = ["La importancia de la ciberseguridad es vital hoy en día", "Necesitamos mejores políticas de seguridad"]

# Modelo Pydantic para recibir el comentario
class Comentario(BaseModel):
    comentario: str

@app.get("/", response_class=HTMLResponse)
async def leer_comentarios(request: Request):
    # Asegúrate de que el nombre de la plantilla es correcto según tu archivo en la carpeta templates
    return templates.TemplateResponse("index.html", {"request": request, "comentarios": comentarios})

@app.post("/agregar")
async def agregar_comentario(comentario: Comentario):
    comentarios.append(comentario.comentario)
    return {"comentarios": comentarios}

# Nuevo endpoint para devolver los comentarios en formato JSON
@app.get("/comentarios-json")
async def comentarios_json():
    return {"comentarios": comentarios}
