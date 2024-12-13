from fastapi import FastAPI
import pandas as pd
from logic import TaskManager

app = FastAPI()
bd_tabla_tareas= pd.DataFrame(columns=TaskManager.DB_COLUMNS)


#filtrar por estado
@app.get("/tareas")
async def root(estado):
    return {"message": "Hello World"}
#crear tarea nueva
@app.post("/tareas")
async def root(nombre_tarea : str, fecha_limite : str):
    return {"message": "Hello World"}
#asignar tarea a usuario
@app.patch("/tareas")
async def root(nombre_tarea : str, id_usuario : str):
    return {"message": "Hello World"}