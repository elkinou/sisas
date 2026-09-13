suma = 0.0
suma_cuadrados = 0.0
N = 0

print("Ingrese números (ingrese -1 para terminar):")

num = float(input("Ingrese un número: "))
while num != -1:
    suma = suma + num
    suma_cuadrados = suma_cuadrados + (num ** 2)
    N = N + 1
    num = float(input("Ingrese un número: "))

if N > 1:
    media = suma / N
    varianza = (suma_cuadrados - (N * (media ** 2))) / (N - 1)
    desviacion = varianza ** 0.5
    print("La desviación estándar muestral es:", desviacion)
else:
    print("Se necesitan al menos 2 números para calcular la desviación estándar muestral.")