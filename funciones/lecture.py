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
