numeros = []

print("Ingrese números (ingrese -1 para terminar):")

num = float(input("Ingrese un número: "))
while num != -1:
    numeros.append(num)
    num = float(input("Ingrese un número: "))

N = len(numeros)

if N > 1:
    suma = 0.0
    for x in numeros:
        suma = suma + x
    media = suma / N

    suma_diferencias = 0.0
    for x in numeros:
        suma_diferencias = suma_diferencias + (x - media) ** 2

    desviacion = (suma_diferencias / (N - 1)) ** 0.5
    print("La desviación estándar muestral es:", desviacion)
else:
    print("Se necesitan al menos 2 números para calcular la desviación estándar muestral.")