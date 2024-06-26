## crear una funcion  que reciba por argumento n numeros 
## y retorne una lista con los numero pares
def num_pares(*args):
    lista_pares=[]
    for n in args:
        if n%2==0:
            lista_pares.append(n)
    return lista_pares
print(num_pares(8,5,4,7,9,25,4,7,12))
#2
def num_pares(*args):
    return[n for n in args if n%2==0 ]
print(num_pares(8,5,4,7,9,25,4,7,12))
# crear tres funciones para los siguientes casos
# calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los numero
# se le pasara por argumento n numeros
def Min(*args):
   menor=args[0]
   for n in args:
    if n<menor:
        menor=n
    return menor
def Max(*args):
    mayor=args[0]
    for n in args:
       if n>mayor:
           mayor=n
    return mayor
def Sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma
valores=4,7,8,5,2,1
print(Min(*valores))
print(Max(*valores))
print(Sum(*valores))
# crear una lista de alumnos com los siguientes campos 
# nombre apellido edad celular email
# 1. actualizar los registros con un campo mas todos tendran el campo 
# de programa de estudio de enfermeria
# 2.buscar el segundo registro u actualizar si edad a 50 años.
# Crear una lista de alumnos con los campos solicitados
alumnos = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 25, "celular": "999888777", "email": "juan@example.com"},
    {"nombre": "Maria", "apellido": "Gomez", "edad": 30, "celular": "666555444", "email": "maria@example.com"}
]

# Actualizar todos los registros con el campo "programa de estudio" de enfermería
for alumno in alumnos:
    alumno["programa de estudio"] = "enfermería"

# Buscar el segundo registro y actualizar su edad a 50 años con filter
segundo_registro = list(filter(lambda x: x["apellido"] == "Gomez", alumnos))[0]
segundo_registro["edad"] = 50

# Imprimir la lista de alumnos actualizada
for alumno in alumnos:
    print(alumno)