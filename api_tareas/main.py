from fastapi import FastAPI
import pandas as pd
from logic import TaskManager
from model import Tarea


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
async def root(tarea: Tarea):
    output = taskManager.create(tarea).to_dict("records")
    return output
#asignar tarea a usuario
@app.patch("/tareas/{task_id}")
async def root(task_id : str, tarea:Tarea):
    output = taskManager.asignar(task_id,tarea).to_dict()
    return output