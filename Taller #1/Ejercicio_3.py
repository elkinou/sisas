frase = input("Ingrese una frase: ")

palabras = frase.split()

invertida_palabras = ""
for i in range(len(palabras) - 1, -1, -1):
    invertida_palabras = invertida_palabras + palabras[i] + " "

invertida_letras = ""
for i in range(len(frase) - 1, -1, -1):
    invertida_letras = invertida_letras + frase[i]

print("Invertida palabra a palabra:", invertida_palabras.strip())
print("Invertida letra a letra:", invertida_letras)