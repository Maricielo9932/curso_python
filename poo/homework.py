# #crear una clase  banco sus atributos seran nombre apellidos deni numero de cuenrta
# #y saldo inicial
# #como metodos podremos hacer deposito retirar dinero y ver estado de cuenta
# class banco:
#     #atributos
#     def __init__(self,nombre,apellidos,dni,numero_de_cuenta,saldo_inicial):
#         self.nombre=nombre
#         self.apellidos=apellidos
#         self.dni=dni
#         self.numero_de_cuenta=numero_de_cuenta
#         self.saldo_inicial=saldo_inicial
#     #metodos
#     def deposito(self):
#         print("estoy depositando 120")
#     def retirar(self):
#         print("estoy retirando 120")
#     def get_status(self):
#         print("estoy viendo el get status actual de mi cuenta")
# mario=banco("mario","ramos lopez",7455125,787998,1220)
# print(mario.deposito())
#Ejercicio 02 I 
# #Crear una clase agencia 
# #con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje 
# #sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje
class agencia:
    #atributos
    def __init__(self,nombre,apellidos,dni,numero_asiento,fecha_viaje):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_asiento=numero_asiento
        self.fecha_viaje=fecha_viaje
    #metodos
    def ingresar_origen(self,lugar):
        print("estoy ingresando de donde viajo:",lugar)
    def ingresar_destino(self):
        print("estoy ingresando de donde voy")
    def cancelar_viaje(self):
        print("estoy cancelando mi viaje ")
    def ver_estado_pasaje(self):
        print("estoy viendo el estado de mi pasaje")
mario=agencia("mario","ramos lopez",7446489,122,"2025-1-22")
print(mario.ingresar_destino())
mario.ingresar_origen("puquio")
