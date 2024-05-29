# lista=["abel","anthony","miguel"]
# print(lista[1:])

# diccionario={"nombre":"antonio","edad":15,"sexo":False}
# print(diccionario["nombre"])

##separa cada caracter
# texto="hola"
# lista_texto=list(texto)
# print(lista_texto)

#trocea cada letra
# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto] #la e es la iteracion que se guardara en cada bucle de texto
# print(lista_texto)

# #trocea cada palabra
# texto_largo="hola como estan bienvenidos al salon"
# nueva_lista=texto_largo.split(" ")
# print(nueva_lista)

# #si quiero de bienvenidos para la derecha
# texto_largo="hola como estan bienvenidos al salon"
# nuevo_texto=texto_largo[16:]
# nueva_lista=nuevo_texto.split(" ")
# print(nueva_lista)

# #separando con indicador "."
# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split(".")
# print(nuevo_texto[-1])

# # .join() es el metodo que usamos para unir elementos de una lista
# # primero va : .join(), luego lo demnas
# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split("") #split quita el ""
# print(" ".join(nuevo_texto)) #quiero que juntes la frase pero con espacio y no con "_"

#quiero convertirlo en lista en bace a un espacio
texto_largo="este es un texto largo chiquita y chiquito"
nuevo_texto=texto_largo.split(" ") #aqui se separa cada palabra en lista []
print(" ".join(nuevo_texto)) #aqui indicamos con que indicador uniremos las palabras
#crear un programa que reciba
#  una lista dessordenada y muestre por 
# terminal la lista ordenada y la lista 
# previa a ser ordenada 
lista=[4,76,1,3,6,8,2]
copia_lista=lista.copy()
copia_lista.sort()
#otra_variable=lista.sort()
print(lista)
print(copia_lista)

