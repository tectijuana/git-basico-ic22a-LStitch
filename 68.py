total = input("Introduce un número positivo menor a 75: ")
arr = []
for x in range(0, int(total)):
    arr.append(int(input("Ingresa un número real: ")))
    
avg = sum(arr) / len(arr)

print("Impresión de números guardados: ")
for num in arr:
    print(num)
print ("El promedio de los números guardados es: " + str(avg))

print("Números dentro del rango de 5 unidades del promedio son: ")
for num in arr:
    if num <= avg + 5 and num >= avg - 5:
        print(num)