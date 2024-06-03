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
