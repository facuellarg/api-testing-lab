import unittest
from logic import TaskManager
import pandas as pd
from model import Responsable
from model import Tarea

class TestTasks(unittest.TestCase):
    def test_When_createtask_Expect_ID(self):
        task = TaskManager()
        tarea = Tarea(
            task = "task",
            date = "01/01/2022",
        )
        db_test =pd.DataFrame()
        returned_id = task.create(db_test, tarea)
        self.assertIsNotNone(returned_id)

    def test_When_filtra_terminados_Expect_lista_tareas(self):
        task = TaskManager()
        state = "terminado"
        db_test = pd.DataFrame({"id":[1],
                                "task":["Prueba"],
                                "date":["23/56/89"],
                                "state":["TO_DO"],
                                "responsable":[None],
                                })
        returned_tasks = task.filter(db_test,state)
        self.assertIsNotNone(returned_tasks)

    def test_When_asinga_usuario_1_a_tarea_1_Expect_tarea_1_con_responsable_1(self):
        task = TaskManager()
        responsable = Responsable(
            responsable="freddy"
        )
        db_test = pd.DataFrame({"id":[1],
                                "task":["Prueba"],
                                "date":["23/56/89"],
                                "state":["TO_DO"],
                                "responsable":[None],
                                })
        db_row = task.assing(db_test,1,responsable)

        self.assertIsNotNone(db_row["responsable"]==responsable)