# averiguar sobre modulos y paquetes en python
Módulos en Python: 
- Un módulo en Python es un archivo que contiene código Python, generalmente funciones, clases y variables.
- Los módulos se utilizan para organizar y reutilizar código en diferentes partes de un programa.
Ejemplo 
```python
# operaciones.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
 ```
Uso de un Módulo:
Para utilizar las funciones definidas en el módulo  operaciones.py , podemos importarlo en otro archivo de la siguiente manera:
```python
import operaciones

resultado_suma = operaciones.suma(5, 3)
print(resultado_suma)  # Output: 8
 ```
Paquetes en Python:
- Un paquete en Python es un directorio que contiene uno o más módulos.
- Los paquetes se utilizan para organizar conjuntos de módulos relacionados en una estructura jerárquica.
 
Ejemplo de Paquete:
 
Supongamos que tenemos un directorio llamado  matematicas  que contiene los módulos  operaciones.py  y  estadisticas.py , junto con un archivo especial  _init_.py  que indica que es un paquete.
```python
matematicas/
    _init_.py
    operaciones.py
    estadisticas.py
 ```
Uso de un Paquete:
 
Para importar un módulo de un paquete en Python, se utiliza la siguiente sintaxis:
 
```python
from matematicas import operaciones

resultado_resta = operaciones.resta(8, 3)
print(resultado_resta)  # Output: 5
```
# diferencia entre modulos y paquetes
- Módulo:
 
- Es un archivo individual que contiene código Python.
- Se utiliza para organizar y reutilizar código en un programa.
- Se importa con la palabra clave  import .
  
- Paquete:
 
- Es un directorio que contiene uno o más módulos.
- Se utiliza para organizar conjuntos de módulos relacionados.
- Debe contener un archivo  _init_.py  para ser reconocido como un paquete.
- Se importa utilizando la ruta del paquete y el nombre del módulo.
 
En resumen, los módulos y los paquetes en Python son fundamentales para la organización y reutilización del código. Los módulos son archivos individuales que contienen código, mientras que los paquetes son directorios que contienen módulos relacionados. La diferencia principal radica en su estructura y organización en el proyecto de software. ¡Explora más sobre módulos y paquetes en Python para mejorar tus habilidades de programación!