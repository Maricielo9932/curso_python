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