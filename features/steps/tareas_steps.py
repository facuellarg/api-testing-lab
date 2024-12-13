import requests
import pandas as pd
from behave import given, when, then


@given(u'un nombre "{task}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given un nombre "tarea01"')


@given(u'una fecha "{date}"')
def step_impl(context, date):
    raise NotImplementedError(u'STEP: Given una fecha "01/01/2024"')


@given(u'un responsables "{responsable}"')
def step_impl(context, responsable):
    raise NotImplementedError(u'STEP: Given un responsable ""')


def verificar_si_esta(tuple_values, db_table):
    return False

def crear_registro(tuple_values, db_table):
    return

@when(u'hacen click en crear una tarea')
def step_impl(context):
    db_tabla_tarea =pd.read_csv(PATH_DB)
    ya_esta = verificar_si_esta(tuple_values, db_tabla_tarea)
    if not ya_esta:
        crear_registro(tuple_values, db_table)



@then(u'responde el identificador de la tarea "{id}"')
def step_impl(context, id):
    raise NotImplementedError(u'STEP: Then responde el identificador de la tarea "1"')