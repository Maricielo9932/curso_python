#WHILE
contador=0
while contador<=5:
    print(contador)
    contador+=1
print(f"valor final {contador}")
#Metodos de string - array 
nombre="jose" 
print(nombre.upper()) # convierte el texto en mayusculas 
apellidos="ALVAREZ" 
print(apellidos.lower()) # convierte el texto a minuscula 
Segundo_nombre="luis" 
#print(segundo_nombre.capitalize()) # convierte la primera letra en mayuscula
#crear un programa que pida la cantidad de notas que se deban registrar luego
#pedira las notas e imprima el promedio
cantidad_notas=int(input("Ingrese la cantidad de notas a registrar: "))
suma_notas = 0
contador = 0
while contador < cantidad_notas:
    nota = float(input(f"Ingrese la nota {contador + 1}: "))
    suma_notas += nota
    contador += 1
promedio = suma_notas / cantidad_notas
if promedio >= 13:
    print(f"El promedio es {promedio:.2f}. ¡Qué genial, tu promedio es excelente!")
else:
    print(f"El promedio es {promedio:.2f}. Sigue esforzándote, ¡tú puedes mejorar!")