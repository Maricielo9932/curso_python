# return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10 y muestre por terminal si es par
#siempre que el valor retone en funcion se utilize en mas
# sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es inpar")
#print solo muestra por terminal
#return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato o un tipo de dato estructurado 
# #crear una funcion que me muestre el producto de dos, numeros
def producto(a,b):
    return a*b
print(producto(a,b))
#crear una funcion que me retorne una lista de tres numeros
def lista_numeros():
    return[3,2,6]
#print usaremos cada vez que muestra funcion retorne un mensaje
#crear una funcion que por parametros recibe un nombre y retorne un mensaje de 
#bienbenida con el nombre.
def mensaje(nombre):
    print(f"hola, (nombre), bienvenida al chongo")
mensaje("jose")
#crear una funcion que reciba por parametro un litas de numero y me devuelve el 
# numero menor mostrar pro terminal el valor retornado por la funcion
lista=(4,5,8,7,3,1)
def min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
        return minimo
print(min(lista))
#crear una funcion que reciba como parametro el nombre y la edad de una persona 
# mi funcion debera retornar un diccionario con los datos, luego mostrar por terminal 
# el valor de retorno de mi funcion
nombre=input("ingrese su nombre delincuente")
edad=int(input("ingrese su edad"))
def persona(nom,edad):
    # return {
    #       "nombre":nom,
    #       "edad":edad
    #  }
    return dict(
        nombre=nom,
        edad=edad
    )
print(persona(nombre,edad))
#empaqueta y desempaqueta de argumento nominales 
def alumnos(**kwargs): 
    kwargs["nombre"]="abel"
    print(kwargs) 
alumnos (nombre= "miguel", apellido="largo", edad=30)
# funciones anonimas (funciones lambda)
lambda:"hola"
print(lambda:"hola")
saludo=lambda:"hola"
print(saludo())
saludo=lambda n,a:"hola",{n} , {a}
print(saludo("ruth","castillo"))
# crear un programa anonimo que reciba como parametro
# una lista de 5 numeros y retorne dos litas una com los
# numeros pares y otra con numeros inpares
litas_numeros=[4,7,5,3,47,2,10,8,10]
pares=lambda l:[n for n in lita if  n%2==0]
impares=lambda l:[n for n in lita if  n%2!==0]
print(pares(lista))
print(inpares(lista))
# tarea hacer el programa de ariba en tres lineas
obtener_pares_impares = lambda numeros: [list(filter(lambda x: x % 2 == 0, numeros)), list(filter(lambda x: x % 2 != 0, numeros))]
lista_pares, lista_impares = obtener_pares_impares([1, 2, 3, 4, 5])
print("Lista de números pares:", lista_pares)
print("Lista de números impares:", lista_impares)
# funciones callback
def mensaje(m): 
    print(m)
def pedir_nombre(): 
    nombre=input("ingresa tu nombre") 
    return nombre 
mensaje(pedir_nombre())