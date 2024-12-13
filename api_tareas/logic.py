import pandas as pd
from model import Tarea
class TaskManager:
    DB_COLUMNS=["id","task","date","state","responsable"] 
    tarea_counter = 0
    def create(self,db,tarea:Tarea):
        new_id = TaskManager.tarea_counter
        db.append(pd.DataFrame({"id":new_id,
                                "task":[tarea.task],
                                "date":[tarea.date],
                                "state":["TO_DO"],
                                "responsable":[tarea.responsable],
                                }))
        TaskManager.tarea_counter += 1
        return new_id
    
    def filtrar(self,db,estado):
        output = db[db["estado"]==estado]
        return output
    
    def asignar(self,db,id_tarea, responsable_id):
        db.loc[db["id"]==id_tarea:"responsable"]=responsable_id
        return (db.loc[db["id"]==id_tarea].reset_index()).iloc[0]
    
