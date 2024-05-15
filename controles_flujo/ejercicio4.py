#crear un programa que eme cuente la cantidad de comas y me muestre
#sus indices.
#ojo:tiene que pedir el uduario
oracion:str= input("Escribe una oración: ")
contador:int=0
for indice,letra in enumerate(oracion):
    if letra == ",":
        print(f"su indice es {indice}")
        contador+=1
print(f"la cantida de comas es{contador}")
#Escribir un programa que pregunte al usuario su edad y muestre 
#por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad:int=int(input("¿Cuántos años tienes? "))
for e in range(edad):
    print("Has cumplido " + str(e+1) + "edad")
# edad = int(input("Ingresa tu edad: "))

for i in range(1, edad+1):
    print("Has cumplido", i, "años")
#crear un programa que me pida el nombre de tres personas 
#y guarde en una variable global la ultima letra de sus nombres 
#y mostrar por pantalla la variable global con las tres ultimas letras del nombre 
# de cada persona utilizando comando for python
# Variable global para almacenar las últimas letras de los nombres
ultimas_letras = ""

# Pedir al usuario el nombre de tres personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    ultima_letra = nombre[-1]  # Obtener la última letra del nombre
    ultimas_letras += ultima_letra  # Concatenar la última letra a la variable global

# Mostrar por pantalla las últimas letras de los nombres de las tres personas
print("Últimas letras de los nombres de las tres personas:")
for letra in ultimas_letras:
    print(letra)
ultima_letra:str=""
for n in range(3):
    nombre:str=input("escribe tu nombre: ")
    #ultima_letra+=nombre[-1]
    last_letter:str=nombre[-1]
    ultima_letra+=last last_letter
    #ultima_letra=ultima_letra+last_letter
    print(ultima_letra)