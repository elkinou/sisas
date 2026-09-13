import math

tolerancia = float(input("Ingrese la tolerancia (epsilon): "))

suma_pi_cuartos = 0.0
n = 0
termino = 1.0

while True:
    denominador = 2 * n + 1
    termino = ((-1) ** n) / denominador
    
    if abs(termino) < tolerancia:
        break
        
    suma_pi_cuartos = suma_pi_cuartos + termino
    n = n + 1

pi_aproximado = 4 * suma_pi_cuartos
error = abs(math.pi - pi_aproximado)

print("Aproximación de pi:", pi_aproximado)
print("Número de términos utilizados:", n)
print("Error absoluto respecto a math.pi:", error)