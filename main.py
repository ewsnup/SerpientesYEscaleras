from auxiliares import *
from Funciones import *

if validar_entrada(input("¿Desea jugar serpientes y escaleras? (S/N): ")):
    
    print("\n=== TRIVIA SERPIENTES Y ESCALERAS ===")
    nombre = input("Ingrese su nombre: ")

    print(f"\n¡Bienvenido al juego, {nombre}!")
    print(f"Comienzas en la posición {pos_actual} del tablero.")

    comenzar = True
    while comenzar:
        # Obtener pregunta y mostrar
        pregunta_actual = obtener_pregunta_aleatoria(preguntas_copia)
        if pregunta_actual == None:
            print("\nYa no hay preguntas.")
            comenzar = False
        mostrar_pregunta(pregunta_actual)

        #Obtiene y valida la respuesta
        respuesta = input("Elige la opción correcta (a, b o c): ").lower()
        es_correcta = validar_respuesta(respuesta, pregunta_actual)

            # Calcular nueva posición
        pos_actual = ejecutar_movimiento(pos_actual, es_correcta, tablero)
        comenzar = fin_del_juego(pos_actual)

        # Preguntar si quiere continuar
        continuar = input("¿Desea seguir jugando serpientes y escaleras? (S/N): ")
        if validar_entrada(continuar) == False:
            print("\nSaliendo del juego...")
            comenzar = False

    print(f"\nJuego terminado. Tu posición final: {pos_actual}")
    guardar_puntaje(nombre, pos_actual)
    print("Tu puntaje ha sido guardado en Score.csv\n")

else:
    print("¡Hasta luego!")
