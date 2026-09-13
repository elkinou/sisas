numeros = []

print("Ingrese números enteros (ingrese -1 para terminar):")

num = int(input("Ingrese un número: "))
while num != -1:
    numeros.append(num)
    num = int(input("Ingrese un número: "))

pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

if len(pares) > 0:
    suma = 0
    for p in pares:
        suma = suma + p
    media = suma / len(pares)
    print("La media de los valores pares es:", media)
else:
    print("No se ingresó ningún número par.")