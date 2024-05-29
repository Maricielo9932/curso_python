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
