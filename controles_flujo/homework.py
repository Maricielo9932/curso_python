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
#Ejercicio Trece
#Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.
# Esta calculadora funciona de la siguiente manera:
# Recogemos los datos A y B
# Si operación es 1 calcula la raíz cuadrada de la suma de A y B
# Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
# Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
# Función para calcular la raíz cuadrada de la suma de A y B
def calcular_raiz_cuadrada_suma(A, B):
    return (A + B) ** 0.5

# Función para calcular A / B
def calcular_division(A, B):
    if B != 0:
        return A / B
    else:
        return "Error: División por cero."

# Función para calcular (A * B) / 2.5
def calcular_formula(A, B):
    return (A * B) / 2.5

# Calculadora interactiva
while True:
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    
    operacion = int(input("Seleccione la operación (1: Raíz cuadrada de la suma, 2: División, 3: Fórmula): "))
    
    if operacion == 1:
        resultado = calcular_raiz_cuadrada_suma(A, B)
    elif operacion == 2:
        resultado = calcular_division(A, B)
    elif operacion == 3:
        resultado = calcular_formula(A, B)
    else:
        print("Operación inválida. Intente de nuevo.")
        continue
    
    print(f"Resultado: {resultado}")
    
    continuar = input("Presione Enter para continuar o escriba 'SAL' para salir: ")
    if continuar == 'SAL':
        break
# Ejercicio Catorce
# Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario login correcto. Sino, llamando ala policía.
# PIN secreto para desbloquear la pantalla
PIN_SECRETO = "1234"
intentos = 3

while intentos > 0:
    intento = input("Ingrese el PIN para desbloquear la pantalla: ")
    
    if intento == PIN_SECRETO:
        print("¡Login correcto!")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"PIN incorrecto. Intentos restantes: {intentos}")
        else:
            print("¡Llamando a la policía!")

# Ejercicio Quince
# Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.
# Función para generar la sucesión de Fibonacci hasta un número dado
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a + b

# Número de elementos de la sucesión de Fibonacci a generar
n = 12
print("Sucesión de Fibonacci:")
fibonacci(n)
#Ejercicio Dieciséis
#Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:

#Debe permitir agregar nuevas tareas a la lista.
#Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
#Debe mostrar la lista actual de tareas pendientes.
#Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
#El menú debe presentar las siguientes opciones:

#Agregar tarea
#Marcar tarea como completada
#Mostrar tareas
#Salir
# Inicialización de la lista de tareas pendientes
tareas_pendientes = []

# Función para agregar una nueva tarea a la lista
def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas_pendientes.append(tarea)
    print("Tarea agregada con éxito.")

# Función para marcar una tarea como completada
def marcar_completada():
    print("Lista de tareas pendientes:")
    for i, tarea in enumerate(tareas_pendientes):
        print(f"{i + 1}. {tarea}")
    
    num_tarea = int(input("Ingrese el número de la tarea completada: "))
    if num_tarea > 0 and num_tarea <= len(tareas_pendientes):
        del tareas_pendientes[num_tarea - 1]
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

# Función para mostrar la lista actual de tareas pendientes
def mostrar_tareas():
    print("Lista de tareas pendientes:")
    for i, tarea in enumerate(tareas_pendientes):
        print(f"{i + 1}. {tarea}")

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        marcar_completada()
    elif opcion == '3':
        mostrar_tareas()
    elif opcion == '4':
        break
    else:
        print("Opción inválida. Intente de nuevo.")
#Ejercicio Diecisiete
#Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:

#Verificar el saldo de su cuenta.
#Depositar dinero en su cuenta.
#Retirar dinero de su cuenta.
#Salir del programa.
#El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:

#Verificar saldo
#Depositar dinero
#Retirar dinero
#Salir
# Saldo inicial predeterminado
saldo = 1000

# Función para verificar el saldo de la cuenta
def verificar_saldo():
    print(f"Saldo actual en la cuenta: ${saldo}")

# Función para depositar dinero en la cuenta
def depositar_dinero():
    monto = float(input("Ingrese el monto a depositar: "))
    global saldo
    saldo += monto
    print("Depósito exitoso.")

# Función para retirar dinero de la cuenta
def retirar_dinero():
    monto = float(input("Ingrese el monto a retirar: "))
    global saldo
    if monto <= saldo:
        saldo -= monto
        print("Retiro exitoso.")
    else:
        print("Saldo insuficiente.")

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        verificar_saldo()
    elif opcion == '2':
        depositar_dinero()
    elif opcion == '3':
        retirar_dinero()
    elif opcion == '4':
        break
    else:
        print("Opción inválida. Intente de nuevo.")
#Ejercicio Dieciocho
#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
# Función para solicitar y validar la contraseña
def validar_contrasena():
    while True:
        contrasena1 = input("Ingrese la con)                 