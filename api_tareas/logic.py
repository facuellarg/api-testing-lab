import pandas as pd
from model import Tarea
from model import Responsable
class TaskManager:
    DB_COLUMNS=["id","task","date","state","responsable"] 
    task_counter = 0
    def create(self,db,task:Tarea):
        new_id = TaskManager.task_counter
        new_task = pd.DataFrame({"id":new_id,
                                "task":[task.task],
                                "date":[task.date],
                                "state":["TO_DO"],
                                "responsable":[task.responsable],
                                })
        db = pd.concat([db,new_task], ignore_index=True)
        TaskManager.task_counter += 1
        return new_id
    
    def filter(self,db,state):
        if len(state) == 0:
            return db.to_json("records")
        output = db[db["state"]== state]
        
        return output
    
    def assing(self,db,id_tarea, responsable:Responsable):

        db.loc[db["id"]==id_tarea,"responsable"]=responsable.responsable
        return (db.loc[db["id"]==id_tarea].reset_index()).iloc[0]
    
