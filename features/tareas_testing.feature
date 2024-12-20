  Feature: Pruebas de la API tareas


  Scenario: Crear tarea con fecha limite
    Given un nombre "tarea01"
    And una fecha "01/01/2024"
    And un responsable "freddy"
    When hacen click en crear una tarea
    Then responde el identificador de la tarea "1"

  Scenario: Asignar tarea a usuario
    Given un id de una tarea "3"
    And un responsable "freddy"
    When  hago una solicitud Patch a "/tareas"
    Then asigna esa tarea al usuario

  Scenario: Filtrar tarea por estado
    Given un estado "testing"
    When hago una solicitud GET a "/tareas"
    Then responde lista de tareas encontradas