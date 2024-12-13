import requests
import json
import pandas as pd
from behave import given, when, then


@given(u'un nombre "{task}"')
def step_impl(context, task):
    context.base_url = "http://localhost:3000/tareas"
    context.task = task


@given(u'una fecha "{date}"')
def step_impl(context, date):
    context.date = date

@given(u'un responsable "{responsable}"')
def step_impl(context, responsable):
    context.base_url = "http://localhost:3000/tareas"
    context.responsable = responsable

def get_task(context):
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(
            f'{context.base_url}?task={context.task}',
            headers=headers
        )
        response.raise_for_status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar el GET: {e}")
        return None

def get_tasks_by_state(context):
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(
            f'{context.base_url}?state={context.state}',
            headers=headers
        )
        response.raise_for_status
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar el GET: {e}")
        return None

def post_task(context, data):  
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        # Realizar petición POST
        response = requests.post(
            context.base_url,
            data=json.dumps(data),
            headers=headers
        )
        
        # Verificar si la petición fue exitosa
        response.raise_for_status()
        
        # Retornar datos creados
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar el POST: {e}")
        return None

def patch_task(context, data, id):  
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        # Realizar petición POST
        response = requests.patch(
            f'{context.base_url}/{id}',
            data=json.dumps(data),
            headers=headers
        )
        
        # Verificar si la petición fue exitosa
        response.raise_for_status()
        
        # Retornar datos creados
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar el POST: {e}")
        return None

@when(u'hacen click en crear una tarea')
def step_impl(context):
    try:
        data = {
            "task":context.task,
            "date":context.date,
            "state":"to-do",
        }

        context.id = post_task(context, data)
    except requests.exceptions.RequestException as e:
        (f"Error al realizar el POST: {e}")
        return None

@then(u'responde el identificador de la tarea "{id}"')
def step_impl(context, id):
    assert context.id is not None


@when(u'hago una solicitud Patch a "/tareas"')
def step_impl(context):
    try:
        task = get_task(context)
        task = task[0]
        data = {
            "id": task['id'],
            "task":task['task'],
            "date":task['date'],
            "state":task['state'],
            "responsable":context.responsable
        }
        context.task_created = patch_task(context,data,task['id'])
    except requests.exceptions.RequestException as e:
        (f"Error al realizar el POST: {e}")
        return None


@then(u'asigna esa tarea al usuaio')
def step_impl(context):
    assert context.task_created['responsable'] == context.responsable

@given(u'un estado "{state}"')
def step_impl(context, state):
    context.base_url = "http://localhost:3000/tareas"
    context.state = state

@then(u'responde lista de tareas encontradas')
def step_impl(context):
    try:
        task = get_tasks_by_state(context)
        print(task)
        assert len(task) == 1
        task = task[0]
        assert task['id'] == '1'
        assert task['task'] ==  "tarea_test"
        assert task['date'] == "01/01/2024"
        assert task['state'] == "testing"
        assert task['responsable'] == "tester"
    except requests.exceptions.RequestException as e:
        (f"Error al realizar el GET: {e}")
        return None

    