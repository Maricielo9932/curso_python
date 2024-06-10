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
>[!WARNING]
>no confudir `print`com `return`, el valor retornado por `return` nos permite usuario fuera de su contexto. y `print()`
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
#retona ("nombre","jose","edad":45)