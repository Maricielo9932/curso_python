# Solicitar al usuario que ingrese su nombre
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Solicitar al usuario que ingrese un número entero
numero_entero = int(input("Ahora, ingresa un número entero: "))

# Imprimir el nombre del usuario tantas veces como el número ingresado
for i in range(numero_entero):
    print(nombre_usuario)
    # Solicitar al usuario que ingrese su nombre completo
nombre_completo = input("Por favor, ingresa tu nombre completo: ")

# Mostrar el nombre completo del usuario tres veces en pantalla
for _ in range(3):
    print(nombre_completo)
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
# Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Por favor, ingresa la edad del cliente: "))

# Calcular el precio de la entrada según la edad del cliente
if edad < 4:
    precio_entrada = 0
elif edad >= 4 and edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Mostrar por pantalla el precio de la entrada
print("El precio de la entrada es: S/.", precio_entrada)
