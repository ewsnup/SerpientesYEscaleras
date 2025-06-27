from auxiliares import *
from funciones import *

if estado_de_juego(input("¿Desea jugar serpientes y escaleras? (S/N): ")):
    
    print("\n=== TRIVIA SERPIENTES Y ESCALERAS ===")
    nombre = input("Ingrese su nombre: ")

    print(f"\n¡Bienvenido al juego, {nombre}!")
    print(f"Comienzas en la posición {pos_actual} del tablero.")

    while True:
        # Obtener pregunta y mostrar
        pregunta_actual = obtener_pregunta_aleatoria(preguntas_copia)
        if pregunta_actual == None:
            print("\nYa no hay preguntas.")
            break
        mostrar_pregunta(pregunta_actual)

        #Obtiene y valida la respuesta
        respuesta = input("Elige la opción correcta (a, b o c): ").lower()
        es_correcta = validar_respuesta(respuesta, pregunta_actual)

            # Calcular nueva posición
        pos_actual = ejecutar_movimiento(pos_actual, es_correcta, tablero)
            
        # Verificar condiciones de fin de juego
        if pos_actual == 0:
            print("\n¡Oh no! Has caído en el casillero perdedor.")
            break
        elif pos_actual == 30:
            print("\n¡Felicidades! Has llegado al casillero ganador.")
            break
            
        # Preguntar si quiere continuar
        continuar = input("¿Desea seguir jugando serpientes y escaleras? (S/N): ")
        if estado_de_juego(continuar) == False:
            print("\nSaliendo del juego...")
            break

    print(f"\nJuego terminado. Tu posición final: {pos_actual}")
    guardar_puntaje(nombre, pos_actual)
    print("Tu puntaje ha sido guardado en Score.csv\n")

else:
    print("¡Hasta luego!")
