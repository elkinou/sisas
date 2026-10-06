n = int(input("Ingrese un entero positivo n: "))

while n <= 0:
    print("El número debe ser positivo.")
    n = int(input("Ingrese un entero positivo n: "))

primos = []

for num in range(2, n + 1):
    es_primo = True
    
    limite = int(num ** 0.5)
    
    for i in range(2, limite + 1):
        if num % i == 0:
            es_primo = False
            break
            
    if es_primo:
        primos.append(num)

print("\nNúmeros primos encontrados menores o iguales que", n, ":")
print(primos)

if len(primos) > 0:
    print("Cantidad de números primos encontrados:", len(primos))
    print("El mayor número primo es:", primos[-1])
else:
    print("No se encontraron números primos en el rango especificado.")
