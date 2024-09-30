#crear una clase de alumnos con los atributos que usted crea conveniente 
#luego instacia a 4 alumnos
class alunmo:
    def __init__(self,nombre,apellido,dni,programa):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.programa=programa
    def mostrar_alumno(self):
        return {
        "nombre":self.nombre,
        "apellido": self.apellido,
        "dni": self.dni,
        "programa":self.programa
        }
# me¿todo
def escribir(self):
    print("estoy escribiendo")
def tarea(self,nombre):
    print("estoy haciendo la tarea de:",nombre)
def terminar_tarea(self):
    print("terminando la tarea anterior")
mario=alunmo("mario","ramos",7455125,"metodologias agiles")
print(mario.nombre)
print(mario.mostrar_alumno())
maru=alunmo("maru","lopez",7895612,"humano")
print(maru.apellido)
king=alunmo("king","zoan ",7464139,"lunaria")
print(king.dni)
maruja=alunmo("marujas","santillan",78915512,"habilidades artisticas")
print(maruja.apellido)
mamu=alunmo("mamuru","santillan",78915512,"habilidades artisticas")
print(mamu.tarea)