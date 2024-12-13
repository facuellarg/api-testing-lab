import pytest
import unittest
from logic import TaskManager
import pandas as pd

class TestTasks(unittest.TestCase):
    def test_When_createtask_Expect_ID(self):
        task = TaskManager()
        returned_id = task.create(pd.DataFrame(columns=["id","task","date","state","responsable"]))
        self.assertIsNotNone(returned_id)
    def test_When_filtra_terminados_Expect_lista_tareas(self):
        task = TaskManager()
        estado = "terminado"
        db_test = pd.DataFrame({"id":[1],
                                "task":["Prueba"],
                                "date":["23/56/89"],
                                "state":["TO_DO"],
                                "responsable":[None],
                                })
        returned_tasks = task.filtrar(db_test,estado)
        self.assertIsNotNone(returned_tasks)

    def test_When_asinga_usuario_1_a_tarea_1_Expect_tarea_1_con_responsable_1(self):
        task = TaskManager()
        responsable="freddy"
        db_test = pd.DataFrame({"id":[1],
                                "task":["Prueba"],
                                "date":["23/56/89"],
                                "state":["TO_DO"],
                                "responsable":[None],
                                })
        db_row = task.asignar(db_test,responsable)

        self.assertIsNotNone(db_row["responsable"]==responsable)