#Ejercicio Siete
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")
# Ejercicio Ocho
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# uNa a una las letras de la palabra introducida empezando por la última.
palabra = input("Ingrese una palabra: ")
print("Letras de la palabra introducida empezando por la última:")
for letra in reversed(palabra):
    print(letra)
#Ejercicio Nueve
#Escriba un programa que pregunte cuántos números se van a introducir, luego pida 
#esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
cantidad_numeros = int(input("Ingrese la cantidad de números a introducir: "))
anterior = float(input("Ingrese el primer número: "))
for i in range(1, cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    if numero <= anterior:
        print("El número ingresado no es mayor que el anterior.")
    anterior = numero