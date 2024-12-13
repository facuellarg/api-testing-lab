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
        return []
    
    def asignar(self,db,tarea_name, responsable_id):
        return True