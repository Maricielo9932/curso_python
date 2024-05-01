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
# Solicitar al usuario que ingrese los dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Comparar los dos números
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero1} es menor que {numero2}")
else:
    print(f"{numero1} es igual a {numero2}")
    
    # Definir los tres números
num1 = 10
num2 = 20
num3 = 30

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado
print("El promedio de los tres números es:", promedio)


# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Validar si el número está en el rango de 1 a 100
if numero >= 1 and numero <= 100:
    print(f"El número {numero} está en el rango de 1 a 100.")
else:
    print(f"El número {numero} no está en el rango de 1 a 100.")
    
    # Definir una función para calcular el volumen de una esfera
radio = float(input("radio: "))
pi = 3.1416
volumen = 4 / 3 * pi * (radio * radio * radio)
print(f'{volumen} m3')

#Calcular el área de un triángulo
 
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
 
area = round((base*altura)/2,2)
 
print("El area del triángulo es: {}".format(area))

# Constante de la velocidad de la luz en metros por segundo
velocidad_luz = 299792458  # m/s

# Distancia promedio de la Tierra al Sol en metros
distancia_sol = 149597870700  # m
# Mostrar el resultado en segundos, minutos, horas y días
print(f"El tiempo total de ida y vuelta al Sol a la velocidad de la luz es de {tiempo_total:.2f} segundos")
print(f"Esto equivale a {tiempo_total/60:.2f} minutos")
print(f"Esto equivale a {tiempo_total/3600:.2f} horas")
print(f"Esto equivale a {tiempo_total/86400:.2f} días")

n = int(input("ingresa un numero: "))
x = 1
c = 0
while x <= n:
	if n % x == 0:
		c = c + 1
	x = x + 1
if c == 2:
	print("el numero ",n," es primo")
else:
	print("el numero ",n," no es primo")
	
	numero_uno:int=int(input('ingresa un numero entero positivo: '))
numero_dos:int=int(input('ingresa segundo numero entero +:'))
if numero_uno == numero_dos:
  print(f'el numero {numero_uno} es igual al numero {numero_dos}')
elif numero_uno != numero_dos:
  if numero_uno*2 == numero_dos:
    print(f'el numero {numero_dos} es el doble del {numero_uno}')
  else:
    print(f'el numero {numero_uno} es distinto al numero {numero_dos}')
    
    # Pedir al usuario que ingrese la longitud del lado del cuadrado
lado = float(input("Ingresa la longitud del lado del cuadrado: "))

# Calcular el área del cuadrado
area = lado ** 2

# Mostrar el resultado
print("El área del cuadrado con lado de longitud", lado, "es:", area)

# Pedir al usuario que ingrese la distancia en kilómetros
kilometros = float(input("Ingresa la distancia en kilómetros: "))

# Factor de conversión de kilómetros a millas (1 kilómetro = 0.621371 millas)
factor_conversion = 0.621371

# Calcular la distancia en millas
millas = kilometros * factor_conversion

# Mostrar el resultado
print(kilometros, "kilómetros equivalen a", millas, "millas")

# Pedir al usuario que ingrese la altura del triángulo
altura = int(input("Ingresa la altura del triángulo: "))

# Dibujar el triángulo de asteriscos
for i in range(1, altura + 1):
    print("*" * i)