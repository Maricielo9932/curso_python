
numeros= {num: True for num in range(2, 73) if all(num % i != 0 for i in range(2, int(num**0.5)+1))}
numeros_primos= list(numeros.keys())[:20]
print(numeros_primos)