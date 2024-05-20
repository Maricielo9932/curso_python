#Ejercicio Uno
#Escribir un programa para una empresa que tiene salas de juegos 
# para todas las edades y quiere calcular de forma automatica el 
# precio que debe cobrar a sus clientes por entrar. El programa 
# debe preguntar al usuario la edad del cliente y mostrar el precio
#  de la entrada. Si el cliente es menor de 4 puede entrar gratis, 
# si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor de 18 deberá
#  pagar 10 soles.
edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10
print(f"El precio de la entrada es: {precio} soles.")
#Ejercicio Dos
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
palabra = input("Ingrese una palabra: ")
for _ in range(10):
    print(palabra)
#Ejercicio Tres
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Ingrese un número entero positivo: "))
impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
resultado = ", ".join(impares)
print(f"Los números impares hasta {numero} son: {resultado}")
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
#Ejercicio Diez
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre
#por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = frase.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la frase.")
#Ejercicio Once
#Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números 
#(que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.
cantidad_numeros = int(input("Ingrese la cantidad de números a introducir: "))
suma = 0
for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero
print(f"La suma de los números introducidos es: {suma}")
#Ejercicio Doce
#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y
#escriba cuántos negativos ha introducido.
cantidad_numeros = int(input("Ingrese la cantidad de números a introducir: "))
contador_negativos = 0
for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    if numero < 0:
        contador_negativos += 1
print(f"Ha introducido {contador_negativos} números negativos.")