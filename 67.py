print("Ingresar número del IMSS")
xx = True
while xx == True:
    n1 = input("Introducir los primeros 3 dígitos por favor: ")
    if len(n1) == 3:
        print("Primeros 3 digitos ingresados correctamente")
        x = n1
        xx = False
    else:
        print("Favor de ingresar los 3 digitos unicamente")

yy = True
while yy == True:
    n2 = input("Introducir los 2 dígitos siguientes por favor: ")
    if len(n2) == 2:
        print("Los siguientes 2 digitos ingresados correctamente")
        y = n2
        yy = False
    else:
        print("Favor de ingresar los 2 digitos unicamente")

zz = True
while zz == True:
    n3 = input("Introducir los siguientes 4 dígitos por favor: ")
    if len(n3) <= 4:
        print("Los siguientes 4 digitos ingresados correctamente")
        z = n3
        zz = False
    else:
        print("Favor de ingresar los 4 digitos unicamente")


print("Tu número del IMMS es: ", x + y + z)