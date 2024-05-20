#CREAR UN PROGRAMA QUE ME MUESTRE LA TABLA DE MULTIPLICAR DE 1 HASTA EL 5
for f in range(1,6):
    multiplicacion=7*f
    print(f'7*{f}={multiplicacion}')
# Mostrar la tabla de multiplicación del 1 al 5
for i in range(1, 6):  # Iterar sobre los números del 1 al 5
    print("Tabla de multiplicar del", i, ":")
    for j in range(1, 11):  # Iterar sobre los números del 1 al 10
        resultado = i * j
        print(i, "x", j, "=", resultado)
    print()  # Salto de línea para separar las tablas

for i in range(1,6): 
    print (f"la tabla de (i)") 
    for j in range(1,13): 
        print("{i}x{j)=(1*j}")
for i in range(1,6):
    print(f"la tabla de (i)") 
    for j in range(1,13): 
        resultado=i*j 
        print(f"{1}x{j}=(resultado)") 
#crear un programa que pida un numero y que muestra la tabla de multiplicar de ese numero
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del número {numero}:")
for m in range(1, 11):
    resultado = numero * m
    print(f"{numero} x {m} = {resultado}")
#while
condicion=True 
while condicion: 
    eval=input("desea continuar (S/N]:")
    if eval.upper()=="S": 
        print("continuas en el bucle") 
        continue 
else: 
    print("se termino el programa") 
    condicion=False
    break
contador=0
while contador<=5:
    print(contador)
    contador+=1
