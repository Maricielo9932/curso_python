ultima_letra:str=""
for n in range(3):
    nombre:str=input("escribe tu nombre: ")
    #ultima_letra+=nombre[-1]
    last_letter:str=nombre[-1]
    ultima_letra+=last_letter
    #ultima_letra=ultima_letra+last_letter
print(ultima_letra)
#crear un programa que muestre la siguiente figura:
#a
#ee
#iii
#oooo
#uuuuu
for i, letra in enumerate("aelou"): 
    print(letra*(1 + 1))
x = 5
for i,char in enumerate(['a', 'e', 'i', 'o', 'u']):
    print(char * (i+1) * x)