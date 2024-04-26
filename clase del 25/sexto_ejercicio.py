#Costo de la sala de juegos
print("ingresa tu edad")
edad = int(input())

if edad < 4:
    print("Tu ingreso es gratis")
elif edad >= 4 and edad < 18:
    print("Tu ingreso cuesta 5 euros")
elif edad >= 18:
    print("Tu ingreso cuesta 10 euros")