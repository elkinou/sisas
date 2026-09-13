n = int(input("Ingrese un número entero positivo (n): "))
while n <= 0:
    print("El número debe ser un entero positivo.")
    n = int(input("Ingrese un número entero positivo (n): "))

b = int(input("Ingrese la base b (2 <= b < 10): "))
while b < 2 or b >= 10:
    print("Base fuera de rango. Debe ser entre 2 y 9.")
    b = int(input("Ingrese la base b nuevamente (2 <= b < 10): "))

numero_original = n
resultado = ""

while n > 0:
    residuo = n % b
    resultado = str(residuo) + resultado
    n = n // b

print("El número", numero_original, "en base", b, "es:", resultado)