from pydantic import BaseModel

class Tarea(BaseModel):
    task: str 
    date: str | None = None
    responsable: str | None = None
    state: str | None = None

class Responsable(BaseModel):
    responsable: str