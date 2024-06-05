#tarea 1
# crear una tisto de 5 alumnas atanacenaresos su nombre opettido y edad 
lista_alumnos[{ 
    "nombre":"abel",
    "apellido": "rojas", 
    "edad":27 
    },{
    "nombre":"cielo",
    "apellido": "castro", 
    "edad":23 
    },{
    "nombre": "ruth", 
    "apellido":"castillo", 
    "edad":18 
    },{
    "nombre":"flor", 
    "apellido":"lucana", 
    "edad":18 
     },{
    "nombre":"rocio", 
    "apellido":"lobo", 
    "edad":25 
}]
#insertor al final de la Lista los datos de antoni 
lista_alumnos.append({ 
    "nombre": "antoni",
    "apellido":"cuevas", 
    "edad":25 
})
print(lista_alumnos) 
#eliminar de la Lista si existe Los datos de obel 
lista_alumnos.remove({ 
    "nombre": "abel", 
    "apellido": "rojas", 
    "edad":27 
}) 
print(lista_alumnos) 
#atuano en la posicion a de Lo indice lista alumnos.
index({ 
"nombre": "rocio", 
"apellido": "lobo", 
"edad":25 
}) 
print(lista_alumnos[indice])
# tarea 2
# Crear una lista con 3 diccionarios de mascotas
mascotas = [
    {"nombre": "Luna", "edad": 3, "sexo": "Hembra", "raza": "Labrador"},
    {"nombre": "Max", "edad": 5, "sexo": "Macho", "raza": "Golden Retriever"},
    {"nombre": "Bella", "edad": 2, "sexo": "Hembra", "raza": "Bulldog"}
]

# Mostrar la lista original
print("Lista Original:")
print(mascotas)

# Editar el tercer registro cambiando la edad
mascotas[2]["edad"] = 4

# Mostrar la lista con el tercer registro modificado
print("\nLista con el Tercer Registro Modificado:")
print(mascotas)
# tarea 3
# un empresario de alquiler de autos desea guardar en una base de datos 
# la informacion de sus vehiculos, proceso que desea automatizar con un 
# sistema infromatico, las acciones que puede realizar el empresario son 
# ver las lista de autos que tiene, podra tambien actualizar la lista y 
# agregar un nuevo vehiculo

# caso de uso de programacion

# yo como empresario
# puedo ver las lista de autos que tengo
# puedo actualizar la lista
# puedo agregar                                                                gar un  nuevo veiculo    
# para guardar informacion de los vehiculos 

# programacion
# Lista de autos
autos = [
    {"marca": "Toyota", "modelo": "Corolla", "año": 2020, "precio": 30000},
    {"marca": "Honda", "modelo": "Civic", "año": 2019, "precio": 28000},
    {"marca": "Ford", "modelo": "Mustang", "año": 2021, "precio": 45000}
]
def ver_lista_autos(lista_autos):
    print("Lista de Autos:")
    for idx, auto in enumerate(lista_autos, 1):
        print(f"Auto {idx}: Marca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}, Precio: ${auto['precio']}")

def actualizar_auto_manual(lista_autos, indice):
    if indice >= 1 and indice <= len(lista_autos):
        print(f"Ingrese la nueva información para el Auto {indice}:")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = int(input("Año: "))
        precio = float(input("Precio: "))
        lista_autos[indice - 1] = {"marca": marca, "modelo": modelo, "año": año, "precio": precio}
        print("Información del auto actualizada correctamente.")
    else:
        print("Índice de auto no válido.")
def agregar_auto(lista_autos, nuevo_auto):
    lista_autos.append(nuevo_auto)
    print("Nuevo auto agregado correctamente.")
ver_lista_autos(autos)
actualizar_auto_manual(autos, 2)
nuevo_auto = {"marca": "Chevrolet", "modelo": "Camaro", "año": 2022, "precio": 50000}
agregar_auto(autos, nuevo_auto)
ver_lista_autos(autos)

# tarea 4 
# crear una lista de los primeros 20 numeros primos haciendo uso de comprension
numeros= {num: True for num in range(2, 73) if all(num % i != 0 for i in range(2, int(num**0.5)+1))}
numeros_primos= list(numeros.keys())[:20]
print(numeros_primos)
