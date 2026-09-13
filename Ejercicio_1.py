import math

opcion = 0

while opcion != 4:
    print("\n--- MENÚ ---")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1 or opcion == 2:
        grados = float(input("Ingrese el valor de x en grados: "))
        x = grados * (math.pi / 180.0)
        
        n_terminos = int(input("Ingrese el número de términos (n): "))
        
        resultado = 0.0

        if opcion == 1:
            for n in range(n_terminos):
                limite_fact = 2 * n + 1
                fact = 1
                for i in range(1, limite_fact + 1):
                    fact = fact * i
                
                termino = ((-1)**n / fact) * (x**(2 * n + 1))
                resultado = resultado + termino
            
            print("El resultado aproximado del Seno es:", resultado)

        elif opcion == 2:
            for n in range(n_terminos):
                limite_fact = 2 * n
                fact = 1
                for i in range(1, limite_fact + 1):
                    fact = fact * i
                
                termino = ((-1)**n / fact) * (x**(2 * n))
                resultado = resultado + termino
            
            print("El resultado aproximado del Coseno es:", resultado)

    elif opcion == 3:
        print("Con esta opción se podría hallar la tangente, pero aún no ha sido implementada.")

    elif opcion == 4:
        print("Saliendo del programa...")

    else:
        print("Opción inválida, intente de nuevo.")