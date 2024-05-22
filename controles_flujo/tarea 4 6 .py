#Ejercicio Cuatro
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()
#Ejercicio Cinco
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.
palabra = input("Ingrese una palabra: ")
print("Letras de la palabra introducida empezando por la última:")
for letra in reversed(palabra):
    print(letra)
#Ejercicio Seis
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#  triángulo rectángulo como el de la imagen adjunta.
numero = int(input("Ingrese un número entero: "))
for i in range(1, numero + 1):
    print("*" * i)
#Ejercicio Siete
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")
