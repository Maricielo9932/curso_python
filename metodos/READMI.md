# metodos en python
## numeros
```python
len (154788) 
# devuelve L cantidad de digitos 
#6
```
## texto
```python
len("hola mundo")
# devuelve la cantidad de caracteres
# el espacio cuenta tambien como un caracter 
# 10 
```
## lista
```python
 len(("h","o"," ", "a")) 
# a devuelve la cantidad de elementos 
# el espacio cuenta tambien como un caracter
``` 
## tuplas
Las tuplas en Python son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables.
```python
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)
```
## dicionario
es una estructura de datos que permite almacenar cualquier tipo de información, desde cadenas de texto o caracteres hasta números enteros, con decimales, listas e incluso otros diccionarios.
```python
import random
clientes = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
diccionario_descuentos = {cliente:random.randint(1,100) for cliente in clientes}
print(diccionario_descuentos)
#Resultado
{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}


