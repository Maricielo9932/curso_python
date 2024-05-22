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