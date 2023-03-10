#retorna apenas numeros pares onde o resto da divisao por 2 = 0
inteiros = [1,2,3,4,5,6,7,8,9,10,11,12]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)