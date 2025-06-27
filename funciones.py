from auxiliares import *
import random

def guardar_puntaje(nombre: str, puntos: int):
    '''Guarda el nombre y el puntaje del jugador.'''
    with open("Score.csv", "a") as puntaje:
        puntaje.write(f"\n{nombre},{puntos}")

def estado_de_juego(respuesta:str) -> bool:
    '''Se le pregunta al usuario si quiere comenzar a jugar 
        o si quiere seguir jugando y valida la respuesta.'''
    respuesta = respuesta.upper()
    while respuesta != "S" and respuesta != "N":
        respuesta = input("Respuesta inválida. Ingrese (S/N): ").upper()
    if respuesta == "S":
        retorno = True
    else:
        retorno = False
    return retorno

def validar_respuesta(respuesta:str, pregunta_actual: dict) -> bool:
    '''Se valida y verifica la entrada del usuario.'''
    while respuesta != "a" and respuesta != "b" and respuesta != "c":
        respuesta = input("Por favor, ingresa solo a, b o c: ").lower()
    
    return respuesta == pregunta_actual["respuesta_correcta"]

def ejecutar_movimiento(pos_actual: int, es_correcta: bool, tablero: list) -> int:
    '''
    Calcula la nueva posición del jugador en el tablero,
    basándose en si su respuesta fue correcta o no.
    '''
    direccion = 1
    if es_correcta == False:
        direccion = -1
    pos_actual += direccion
    while tablero[pos_actual] != 0:
        pos_actual += (tablero[pos_actual] * direccion)

    if es_correcta:
        print(f"¡Correcto! Nueva posición: {pos_actual}\n")
    else:
        print(f"¡Incorrecto! Nueva posición: {pos_actual}\n")
    
    return pos_actual

def obtener_pregunta_aleatoria(preguntas_copia: list) -> bool:
    '''Se selecciona una pregunta aleatoria y se remueve la pregunta ya hecha'''
    pregunta_actual = None 
    
    if preguntas_copia: 
        pregunta_actual = random.choice(preguntas_copia)
        preguntas_copia.remove(pregunta_actual)
    
    return pregunta_actual

def mostrar_pregunta(pregunta: list):
    '''Muestra la pregunta y sus opciones de respuesta'''
    print("\n" + pregunta["pregunta"])
    print(f"a) {pregunta['respuesta_a']}")
    print(f"b) {pregunta['respuesta_b']}")
    print(f"c) {pregunta['respuesta_c']}")
