import pandas as pd

class TaskManager:
    DB_COLUMNS=["id","task","date","state","responsable"] 
    tarea_counter = 0
    def create(self,db,nombre_tarea, fecha_limite):
        new_id = TaskManager.tarea_counter
        db.append(pd.DataFrame({"id":[new_id],
                                "task":[nombre_tarea],
                                "date":[fecha_limite],
                                "state":["TO_DO"],
                                "responsable":[None],
                                }))
        TaskManager.tarea_counter += 1
        return new_id
    
    def filtrar(self,db,estado):
        output = db[db["estado"]==estado]
        return output
    
    def asignar(self,db,tarea, responsable_id):
        db.loc[db["task"]==tarea:"responsable"]=responsable_id
        return (db.loc[db["task"]==tarea].reset_index()).iloc[0]
    
