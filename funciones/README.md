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