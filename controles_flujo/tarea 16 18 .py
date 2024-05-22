#Ejercicio Dieciséis
#Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:

#Debe permitir agregar nuevas tareas a la lista.
#Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
#Debe mostrar la lista actual de tareas pendientes.
#Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
#El menú debe presentar las siguientes opciones:

#Agregar tarea
#Marcar tarea como completada
#Mostrar tareas
#Salir
# Inicialización de la lista de tareas pendientes
tareas_pendientes = []

# Función para agregar una nueva tarea a la lista
def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas_pendientes.append(tarea)
    print("Tarea agregada con éxito.")

# Función para marcar una tarea como completada
def marcar_completada():
    print("Lista de tareas pendientes:")
    for i, tarea in enumerate(tareas_pendientes):
        print(f"{i + 1}. {tarea}")
    
    num_tarea = int(input("Ingrese el número de la tarea completada: "))
    if num_tarea > 0 and num_tarea <= len(tareas_pendientes):
        del tareas_pendientes[num_tarea - 1]
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

# Función para mostrar la lista actual de tareas pendientes
def mostrar_tareas():
    print("Lista de tareas pendientes:")
    for i, tarea in enumerate(tareas_pendientes):
        print(f"{i + 1}. {tarea}")

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        marcar_completada()
    elif opcion == '3':
        mostrar_tareas()
    elif opcion == '4':
        break
    else:
        print("Opción inválida. Intente de nuevo.")
#Ejercicio Diecisiete
#Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:

#Verificar el saldo de su cuenta.
#Depositar dinero en su cuenta.
#Retirar dinero de su cuenta.
#Salir del programa.
#El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:

#Verificar saldo
#Depositar dinero
#Retirar dinero
#Salir
# Saldo inicial predeterminado
saldo = 1000

# Función para verificar el saldo de la cuenta
def verificar_saldo():
    print(f"Saldo actual en la cuenta: ${saldo}")

# Función para depositar dinero en la cuenta
def depositar_dinero():
    monto = float(input("Ingrese el monto a depositar: "))
    global saldo
    saldo += monto
    print("Depósito exitoso.")

# Función para retirar dinero de la cuenta
def retirar_dinero():
    monto = float(input("Ingrese el monto a retirar: "))
    global saldo
    if monto <= saldo:
        saldo -= monto
        print("Retiro exitoso.")
    else:
        print("Saldo insuficiente.")

# Menú interactivo
while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        verificar_saldo()
    elif opcion == '2':
        depositar_dinero()
    elif opcion == '3':
        retirar_dinero()
    elif opcion == '4':
        break
    else:
        print("Opción inválida. Intente de nuevo.")
#Ejercicio Dieciocho
#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
# Función para solicitar y validar la contraseña
def validar_contrasena():
    while True:
        contrasena1 = input("Ingrese la con)                 