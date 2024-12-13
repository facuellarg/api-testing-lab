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
    context.responsable = responsable


def verificar_si_esta(context):
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(
            f'{context.base_url}?task={context.task}',
            headers=headers
        )
        response.raise_for_status
        return len(response.json()) > 0
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar el GET: {e}")
        return None


def crear_registro(context):
    data = {
        "task":context.task,
        "date":context.date,
    }
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


@when(u'hacen click en crear una tarea')
def step_impl(context):
    try:
        esta = verificar_si_esta(context)
        assert not esta
        context.id = crear_registro(context)
    except requests.exceptions.RequestException as e:
        (f"Error al realizar el POST: {e}")
        return None

@then(u'responde el identificador de la tarea "{id}"')
def step_impl(context, id):
    assert context.id is not None