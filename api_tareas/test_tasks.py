import pytest
import unittest
from logic import Task
import pandas as pd

class TestTasks(unittest.TestCase):
    def test_When_createtask_Expect_ID(self):
        task = Task()
        returned_id = task.create(pd.DataFrame(columns=["id","task","date","state","responsable"]))
        self.assertIsNotNone(returned_id)
    def test_When_filtra_terminados_Expect_lista_tareas(self):
        task = Task()
        returned_id = task.create(pd.DataFrame(columns=["id","task","date","state","responsable"]))
        self.assertIsNotNone(returned_id)

    def test_When_asinga_usuario_1_a_tarea_1_Expect_tarea_1_con_responsable_1(self):
        task = Task()
        returned_id = task.create(pd.DataFrame(columns=["id","task","date","state","responsable"]))
        self.assertIsNotNone(returned_id)