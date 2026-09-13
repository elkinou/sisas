numeros = []

print("Ingrese números enteros (ingrese -1 para terminar):")

num = int(input("Ingrese un número: "))
while num != -1:
    numeros.append(num)
    num = int(input("Ingrese un número: "))

if len(numeros) == 0:
    print("No se ingresaron números.")
else:
    # 1. Encontrar la mayor cantidad de repeticiones (frecuencia máxima)
    max_frecuencia = 0
    for x in numeros:
        conteo = 0
        for y in numeros:
            if x == y:
                conteo = conteo + 1
        if conteo > max_frecuencia:
            max_frecuencia = conteo

    # 2. Caso donde ningún número se repite
    if max_frecuencia == 1:
        print("Ningún valor se repite (no existe moda en la lista).")
    else:
        # 3. Buscar todos los números que tienen la frecuencia máxima (sin duplicados)
        modas = []
        for x in numeros:
            conteo = 0
            for y in numeros:
                if x == y:
                    conteo = conteo + 1
            if conteo == max_frecuencia and x not in modas:
                modas.append(x)

        # 4. Mostrar resultados según si es unimodal o multimodal
        if len(modas) == 1:
            print("El conjunto es unimodal. La moda es:", modas[0])
        else:
            print("El conjunto es multimodal. Las modas son:", modas)