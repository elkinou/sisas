numero = input("Ingrese un entero positivo: ")

resultado = ""

for i in range(len(numero)):
    resultado = resultado + numero[i]
    if i != len(numero) - 1:
        resultado = resultado + "0"

print("El número con ceros intercalados es:", resultado)