import random
n = int(input("Ingresar cuantos números de dos dígitos quieres generar: "))
edad = int(input("Ingresa tu edad: "))
numeros = []
for x in range(0, n):
    numeros.append(random.randint(10, 99))
print("Estos son los números generados: ", numeros)

print("\n\nEstos son los números menores a tu edad: ")
for num in numeros:
    if num < edad:
        print(num)
