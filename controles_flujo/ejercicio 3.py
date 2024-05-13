#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla
#la cuenta atrás desde ese número hasta cero separados por comas.a

# Pedir al usuario un número entero positivo
numero = int(input("Por favor, ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if numero < 0:
    print("El número ingresado no es positivo.")
else:
    # Crear una lista con los números desde el número ingresado hasta 0
    cuenta_atras = list(range(numero, -1, -1))
    
    # Convertir la lista en una cadena separada por comas
    cuenta_atras_str = ', '.join(map(str, cuenta_atras))
    
    # Mostrar la cuenta atrás por pantalla
    print("Cuenta atrás:", cuenta_atras_str)