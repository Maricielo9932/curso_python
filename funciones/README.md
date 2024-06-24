# FUNCIONES
matematicamente una funcion es una operacion 
que toma uno om mas valores llamados `argumentos`
y produce un valor denominado resultado.
f(x)=x/1+x**2
>[!NOTE]
>todos los lenguajes de programacion tienen 
funciones incorporadas (`funciones internas`), y funciones creadas por el usuario (`fuciones externas`)
en programacion una funcion es un subprograma, es una estrutura que nos permite agrupar codigo y sus principales objetivos son 
-`NO REPETIR` fragmetos de codigos 
-`REUTILIZAR` el codigo en distitos esenarios 
## Estrutura de una funcion
Una funcion viene definida por un nombre, sus `parametros` y su valor de `retorno` una ves creada la funcion podremos solcitar su ejecucion `invocando` la funcion por su `nombre`.
## Definir una funcion en python
para definir una funcion en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. a continuacion especificaremos los `parametros` con `()` si es una funcion sin parametros `(a)` si es una funcion con parametros, si se tuviera mas de un parametro iran separados por `,`, finalizremos con linea `:`, en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (micro programa)que puede contener 1 o mas sentencias, finalmente devera `retornar` un resultado con la palabra reservada `return`.
>[!TIP]
>como retorno tambien se puede utilizar la `funcion interna`, print()`, para depuracion de codigo no es recomendado usalo en produccion .
print detro de una funcion es una herramienta para depurar o comprobar que una funcion este haciendo el trabajp de una maneras correcta 
**ejemplo**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"(saludo), {saludo_dos}"
    #print(f"(saludo), {saludo_dos}")
print(saludo())
#saludo()
```
## Invocar una funcion 
para invocar una funcion (o llama, ejecutar) una funcion solo tendremos que escribir el `nombre`de la  una funcion seguido por`()` parentesis
```python
def saludo():
    print("hola")
#invocando lafuncion
saludo()
```
## retonar un valor
las funciones pueden retonar (o devolver)un valor.
```python
def uno():
    return 1
uno()
```
>[!WARNING]o confudir `print`com `return`, el valor retornado por `return` nos permite usuario fuera de su contexto. y `print()`
solo mostrara el literal poe terminal.
**ejemplo**
*en el archivo `lecture.py`
## Retornar multiples valores
El secreto es hacerlo mediante un tipo de datos estruturados
```python
def varios():
    return 2,3,4
varios()
#retona(2,3,4)
def lista():
    return["hola",45]
#retona["hola",45]
def dicc():
    return("nombre","jose","edad":45)
dicc()
#retona ("nombre","jose","edad":45) 2
```
## parametros y argumentos
si una funcio no dispusiera de valores de entrada estaria limitada en su actuacion.
es por ello que los `parametro` no permiten variar los datos que comsume para obtener 
distintos resultado
**ejemplo**
*crear una funcion que recibee un valornumerico y devuelve su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA:en este caso, el valor 4 es un argumento de la funcion 
sqrt(4)
```
cundo llama,os una funcion con los `argumentos`, los valores de estos argumentos se 
copian en los correspondientes `parametros` dentro de la funcion.
```python
def ejem(a,b,c):
    return a+b+c
ejem(4,5,6)
```
### argumentos nominales
en esta aproximacion los argumentos no son copiados  en un orden especifico sino que 
**se asignanpor nombre a cada parametro**. ello nos permite evitar el problema de conocer
o recordar cual es el orden de los parametros de la funcion. 
para utilizarlo basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia}, 
    con {num_core}, cores y con una 
    frecuencia {frecuencia} """)
    build_cpu(num_core=4,familia="intel",frecuencia=2.7)
```
### argumentos posicionales
los argumentos son copiados en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia},
    con {num_core}, cores y con una 
    frecuencia de (frecuencia) 
    """)
#haciendo uso de agumentos posicionales
build_cpu("intel",4,2,7)
```
### parametros por defecto
es posible especificar *valores por defecto* en los parametros de una funcion, en el caso de que no se proporcione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto
**ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("anthony","cruces","desaprobados")
```
### desempaquetado/empaquetado de argumentos(tarea)
son argumentos cuando estamos invocando a una función, tanto para argumentos posicionales como para argumentos nominales.
Y de esto se deriva el hecho de que podamos utilizar un número variable de argumentos en una función, algo que puede ser muy interesante según el caso de uso que tengamos.
- Empaquetar/Desempaquetar argumentos posicionales
- empaquetado posicionales
**ejemplo**
```python
def calcular_promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio
print(calcular_promedio(5, 10, 15))  
print(calcular_promedio(2, 4, 6, 8, 10))  
```
- desenpaquetado posicionales 
```python
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años.")
datos = ["María", 30]
saludar(datos) 
info = {"nombre": "Juan", "edad": 25}
saludar(info) 
```
- Empaquetar/Desempaquetar argumentos nominales
- Empaquetar nominales
**ejemplo**
```python
def imprimir_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
info = {"nombre": "María", "edad": 30, "ciudad": "Lima"}
imprimir_info(**info) 
```
- Desempaquetar nominales
```python
def saludar(**info):
    if "nombre" in info and "edad" in info:
        print(f"Hola {info['nombre']}, tienes {info['edad']} años.")
datos = {"nombre": "Juan", "edad": 25}
saludar(**datos) 
```
### funciones internas de python(tarea)
también conocidas como funciones anidadas son funciones definidas dentro de otra función. Estas funciones internas pueden acceder a las variables locales de la función externa en la que están definidas. 
```python
 Copiar
def funcion_externa():
    mensaje = "Hola, soy una función externa."

    def funcion_interna():
        print("Soy una función interna.")
    
    funcion_interna() 
    print(mensaje)  
funcion_externa()
```
## tipos de funciones 
-Funciones integradas (Built-in Functions): 
Son funciones predefinidas en Python que están disponibles para su uso sin necesidad de importar ningún módulo adicional. Ejemplos de funciones integradas son  print() ,  len() ,  max() ,  min() 
```python
# Función integrada para obtener la longitud de una lista
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print("Longitud de la lista:", longitud)
```
-Funciones definidas por el usuario (User-defined Functions): 
Son funciones creadas por el usuario para realizar tareas específicas. Estas funciones se definen utilizando la palabra clave  def .
```python
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print("Resultado de la suma:", resultado)
```
## funciones anonimas (funciones lambda)
-Funciones lambda (Lambda Functions): 
Son funciones anónimas que pueden tener cualquier número de argumentos pero solo pueden tener una expresión. Se definen utilizando la palabra clave  lambda .
```python
# Función lambda para calcular el cuadrado de un número
cuadrado = lambda x: x**2
resultado = cuadrado(5)
print("Cuadrado de 5:", resultado)
 ``` 
### funciones closure
Una función de cierre (closure) en Python es una función que recuerda el ámbito en el que fue creada, incluso cuando la función se está ejecutando fuera de ese ámbito. Esto significa que la función de cierre puede acceder y recordar las variables locales de la función externa en la que fue definida.
```python
def multiplicador(n):
    def funcion_interna(x):
        return x * n
    return funcion_interna

# Crear funciones de cierre con diferentes valores
multiplicar_por_2 = multiplicador(2)
multiplicar_por_5 = multiplicador(5)

# Utilizar las funciones de cierre
resultado1 = multiplicar_por_2(10)
resultado2 = multiplicar_por_5(10)

print("Resultado de multiplicar 10 por 2:", resultado1)
print("Resultado de multiplicar 10 por 5:", resultado2)
```
### funciones callback
En Python, las funciones de devolución de llamada (callback functions) son funciones que se pasan como argumentos a otras funciones para que se ejecuten en un momento específico o en respuesta a ciertas acciones. Las funciones de devolución de llamada son comunes en programación asíncrona, manejo de eventos y programación orientada a objetos.
```python
def operacion_matematica(a, b, callback):
    resultado = a + b
    callback(resultado)

def mi_callback(resultado):
    print("El resultado de la operación es:", resultado)

# Llamada a la función con una función de devolución de llamada
operacion_matematica(5, 3, mi_callback)
```
### programacion 
La programación en Python es el proceso de escribir instrucciones en el lenguaje de programación Python para crear programas que realicen tareas específicas. Python es un lenguaje de programación popular y versátil que se utiliza en una amplia gama de aplicaciones, como desarrollo web, análisis de datos, inteligencia artificial, automatización, entre otros.
```python
print("¡Hola, mundo!")
# programacion interativa
lista =[5,7,8,4,1]
def num minimo(1): 
    minimo=l[0] 
    for n in l: 
        if < n minimo: 
            minimo-n  
    return minimo
#programcion funcional
min(lista)
 ```
En este ejemplo,  print()  es una función integrada en Python que imprime el texto "¡Hola, mundo!" en la consola cuando se ejecuta el programa.
La programación en Python implica escribir código en un editor de texto o un entorno de desarrollo integrado (IDE), guardar el archivo con la extensión  .py  y luego ejecutar el programa para ver el resultado. Los programas en Python pueden incluir funciones, condicionales, bucles, manejo de excepciones y mucho más para crear aplicaciones complejas.

#### averiguar sobre map(), filter(), reduce()
### 1.  map : La función  map  aplica una función a cada elemento de una lista y devuelve un nuevo iterable con los resultados.
 
Ejemplo de  map :
 
python
 Copiar
# Doble de cada número en una lista
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros))
print(resultado)  # Output: [2, 4, 6, 8, 10]
 
 
### 2.  filter : La función  filter  filtra los elementos de una lista según una condición especificada en una función.
 
Ejemplo de  filter :
 
python
 Copiar
# Filtrar los números pares de una lista
numeros = [1, 2, 3, 4, 5]
resultado = list(filter(lambda x: x % 2 == 0, numeros))
print(resultado)  # Output: [2, 4]
 
 
### 3.  reduce : La función  reduce  aplica una función de manera acumulativa a los elementos de una lista, reduciéndola a un solo valor.
 
Antes de Python 3,  reduce  estaba disponible directamente, pero ahora se encuentra en el módulo  functools .
 
Ejemplo de  reduce :
 
python
 Copiar
from functools import reduce

# Suma de todos los elementos de una lista
numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)  # Output: 15
