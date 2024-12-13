from fastapi import FastAPI
import pandas as pd
from logic import TaskManager

app = FastAPI()
bd_tabla_tareas= pd.DataFrame(columns=TaskManager.DB_COLUMNS)
taskManager=TaskManager()

#filtrar por estado
@app.get("/tareas")
async def root(estado):
    output=taskManager.filtrar(bd_tabla_tareas,estado).to_dict("records")
    return output
#crear tarea nueva
@app.post("/tareas")
async def root(nombre_tarea : str, fecha_limite : str):
    output = taskManager.create(nombre_tarea,fecha_limite).to_dict("records")
    return output
#asignar tarea a usuario
@app.patch("/tareas")
async def root(id_tarea : str, id_usuario : str):
    output = taskManager.asignar(id_tarea,id_usuario).to_dict()
    return output