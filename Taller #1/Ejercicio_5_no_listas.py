suma_pares = 0
cantidad_pares = 0

print("Ingrese números enteros (ingrese -1 para terminar):")

num = int(input("Ingrese un número: "))
while num != -1:
    if num % 2 == 0:
        suma_pares = suma_pares + num
        cantidad_pares = cantidad_pares + 1
    num = int(input("Ingrese un número: "))

if cantidad_pares > 0:
    media = suma_pares / cantidad_pares
    print("La media de los valores pares es:", media)
else:
    print("No se ingresó ningún número par.")