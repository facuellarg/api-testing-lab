  Feature: Pruebas de la API tareas


  Scenario: Crear tarea con fecha limite
    Given un nombre "tarea01"
    And una fecha "01/01/2024"
    And un responsable "freddy"
    When hacen click en crear una tarea
    Then responde el identificador de la tarea "1"