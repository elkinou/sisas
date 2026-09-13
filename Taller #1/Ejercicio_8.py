a = float(input("Ingrese la longitud del primer lado (0 para salir): "))

while a != 0:
    if a < 0:
        print("La longitud debe ser positiva. Intente de nuevo.")
    else:
        b = float(input("Ingrese la longitud del segundo lado: "))
        c = float(input("Ingrese la longitud del tercer lado: "))

        if b <= 0 or c <= 0:
            print("Las longitudes deben ser positivas mayores a cero.")
        else:
            if (a + b > c) and (a + c > b) and (b + c > a):
                if a == b and b == c:
                    tipo_lado = "Equilátero"
                elif a == b or a == c or b == c:
                    tipo_lado = "Isósceles"
                else:
                    tipo_lado = "Escaleno"

                mayor = a
                l2 = b
                l3 = c

                if b > mayor:
                    mayor = b
                    l2 = a
                    l3 = c
                if c > mayor:
                    mayor = c
                    l2 = a
                    l3 = b

                cuadrado_mayor = mayor ** 2
                suma_cuadrados = (l2 ** 2) + (l3 ** 2)

                if abs(cuadrado_mayor - suma_cuadrados) < 1e-9:
                    tipo_angulo = "Rectángulo"
                elif cuadrado_mayor < suma_cuadrados:
                    tipo_angulo = "Acutángulo"
                else:
                    tipo_angulo = "Obtusángulo"

                print("Es un triángulo válido.")
                print("Clasificación por lados:", tipo_lado)
                print("Clasificación por ángulos:", tipo_angulo)
            else:
                print("No forma un triángulo válido (no cumple la desigualdad triangular).")

    print("\n----------------------------------------")
    a = float(input("Ingrese la longitud del primer lado (0 para salir): "))

print("Saliendo del programa...")