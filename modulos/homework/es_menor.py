def es_menor(lista:list)
    """funcion para saber si el numero mayor de una lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
            menor=n
            return menor