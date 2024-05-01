# Solicitar al usuario que ingrese su nombre
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Solicitar al usuario que ingrese un número entero
numero_entero = int(input("Ahora, ingresa un número entero: "))

# Imprimir el nombre del usuario tantas veces como el número ingresado
for i in range(numero_entero):
    print(nombre_usuario)
# Solicitar al usuario que ingrese un número de teléfono en el formato +34-XXXXXXXXX-XX
telefono = input("Por favor, ingresa un número de teléfono en el formato +34-XXXXXXXXX-XX: ")

# Separar el número de teléfono en prefijo, número y extensión
prefijo, numero, extension = telefono.split('-')

# Mostrar por pantalla el número de teléfono sin el prefijo y la extensión
print("Número de teléfono sin prefijo ni extensión:", numero)
# Solicitar al usuario que ingrese su nombre y sexo
nombre = input("Por favor, ingresa tu nombre: ")
sexo = input("Ahora, ingresa tu sexo (M para masculino, F para femenino): ")

# Convertir el nombre a minúsculas para facilitar la comparación
nombre = nombre.lower()

# Determinar el grupo al que pertenece el alumno
if (sexo == 'F' and nombre < 'm') or (sexo == 'M' and nombre > 'n'):
    grupo = 'A'
else:
    grupo = 'B'

# Mostrar por pantalla el grupo al que pertenece el alumno
print("El grupo al que perteneces es:", grupo)
# Calcular el tiempo de ida al Sol (ida = distancia / velocidad)
tiempo_ida = distancia_sol / velocidad_luz
