from pydantic import BaseModel

class Tarea(BaseModel):
    id:str
    task: str
    date: str | None = None
    responsable: str | None = None
    state: str | None = None