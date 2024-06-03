# TIPOS DE DATOS ESTRUCTURADOS (TDA - TIPOS DE DATOS ABSTRACTOS)
 python
#listas []
## sus valores o elementos se pueden actualizar o eliminar
## tanto listas con o las tuplas todos los elementos que se crean python crea indices (negativo y positivo)
```python
lista=["nombre",20,2,3,False,["texto,.2"]]
```
# tupla ()
## sus valores o elementos no pueden ser modificados o eliminados
### la lista que esta dentro de una tupla no puede modificarse
## tanto listas con o las tuplas todos los elementos que se crean python crea indices (negativo y positivo)
```python
tupla=("ruth",20,2,3,False,[])
```
#diccionarios {} (en yava se conoce como OBJETOS)
## los diccionarioas almacenan los datos con clave:valor
```python
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
- [!TIP]
- *Observacion:* que los tipos de datos estructurados pueden almacenar enm su interior otros tipos de datos estructuarados

```python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20,
        "amigos":[no tiene]
    },{
        "nombre":"ruth",
        "edad":13,
        "amigos":["flor","rocio"]
    }
    ]
    #terminar de copiar

```
## Metodos
### 1. Convertir texto a lista
 ```python
#Metodo list
texto="hola"
list(texto) #["h","o","l","a"]
```
# 1. Metodo split
#separa cada caracter de la lista
texto="hola como estan,alumnitos lindos"
texto.split(",")
#los elementos se separan por comas
#trocea textos en listas a partir de un limitador (espacios, comas ",") o sea: *"hola como estan*  es uno y el otro es *alumnitos lindos"*, porque el limiytador es una coma ",", es depende de cada uno los indicadores    que ponemos

# 2. Metodo join
```python
texto_largo="este es un texto largo chiquita y chiquito"
nuevo_texto=texto_largo.split(" ") #aqui se separa cada palabra en lista []
print(" ".join(nuevo_texto)) #aqui indicamos con que indicador uniremos las palabras
```
### 2. Agregar elementos a una lista
 python
# 1. Metodo append - es el metodo que me permite agregar elementos alñ final de una lista
# en jaya se le coonoce como git "push" (o sea sube a la nuve)
lista=["hola"]
lista.append("mundo")
print(lista) #["hola","mundo"]

# 2. Metodo insert - es el metodo que me permite agregar elementos en cualquier ubicacion de mi lista
#parametros: 1. indice o posision en la que agregare el texto (0) y 2. texto que voy a agregar "texto"
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0:"rocio") #["rocio","edith","ruth","luz"]

# 3. Metodo pop - es el metodo que elimine el ultimo elemento de una lista, es lo contrario a append.
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop() #["edith","ruth"]

# Primera opcion - Metodo remove - este metodo elimine el por el nombre el elememto que coincida dentro de mi lista
#elimina por nombre o texto
lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# Segunda opcion - Metodo pop - al pasarle por parametro un indice este lo eliminara de la lista
# elimina por indice
# si a pop no le especificas un indice por defecto elimina el ultimo
```python
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)
```
# 4. Buscar un elemento en una lista .index (se usa para informacion grande)
```python
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombre[indice])
```
pertenencia="edith" in lista_nombres #True False
### 5. comparacion de listas 
podemos haecer uso de los operadores de conparacion para comparar  listas 
**ejem**
```python
compara=[1,2,3]>[1,2,4] 
 # no por no se 97 
 # no por que son iguales en ambas listas 
 # evalua que es menor a 4 
 # entonces la primera lista es menor que la segunda lista
print(compara) 
# salida:
```
### 6. cuidados con las copiasI
### 7. fe de errtas (actualizar listas)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(copia_lista)
#[2,3,4,5,6]
#mofificar la lista con dicionario
alummnos=[
    (
        "nombre":"abel
        "edad":15
    ),
    ( 
        "nomnbre":"anthony",
        "edad":29
    )
]
alummnos[0]["edad"]=10
alummnos[0]=("nombre":"mafer","edad":15)
alummnos[1]["sexo"]=" por defenir"
print(alumnos)
```

