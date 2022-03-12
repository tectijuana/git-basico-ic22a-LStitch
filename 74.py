import random

numeros = []
print("Numeros generados:")
for x in range(0, 20):
    num = (random.randint(1, 100))
    print(num)
    numeros.append(num)
    
numeros.sort()

print("\nParejas impresas")
while(len(numeros)!=0):
    print(numeros[-1], numeros[0])
    del numeros[-1]
    del numeros[0]