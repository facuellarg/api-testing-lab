from fastapi import FastAPI
import pandas as pd
from logic import TaskManager
from model import Tarea
from model import Responsable


app = FastAPI()
init_values =  [{
    "id": "1",
    "task": "tarea_test",
    "date": "01/01/2024",
    "state": "testing",
    "responsable": "tester"
},
{
    "id": "2",
    "task": "tarea_test2",
    "date": "01/01/2024",
    "state": "testing invalid",
    "responsable": "tester"
},
{
    "id": "3",
    "task": "tarea_test2",
    "date": "01/01/2024",
    "state": "testing invalid",
    "responsable": "other invalid"
},
]
db_tasks= pd.DataFrame(init_values)

taskManager=TaskManager()

#filtrar por estado
@app.get("/tareas")
async def root(state:str):
    output=taskManager.filter(db_tasks,state).to_dict("records")
    return output
#crear tarea nueva
@app.post("/tareas")
async def root(task: Tarea):
    id = taskManager.create(db_tasks,task)
    return id
#asignar tarea a usuario
@app.patch("/tareas/{task_id}")
async def root(task_id : str, responsable:Responsable):
    output = taskManager.assing(db_tasks, task_id, responsable).to_dict()
    return output