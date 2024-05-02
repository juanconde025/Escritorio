"""
Escribir un programa que tenga un menú interactivo que se repite hasta que el usuario diga salir, 
las opciones del menú son:

-Verificar si un número es primo
-Verificar si un número es par o impar
-Obtener la media de una serie de números
-Verificar si una palabra contiene la letra x o z

Cada proceso de las opciones del menú deben implementarse en una función.
"""

#Verificar si un número es primo
def primo (num):
    contador = 2
    resultado = True     
    while (contador <= num/2 and resultado):         
        resultado = num % contador != 0
        contador+= 1
    return resultado
#Verificar si un número es par o impar
def par (num):
    return num%2==0
#Obtener la media de una serie de números
def media(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma/len(lista)

def generar_lista():
    cantidad = (int(input("Ingrese cuantos valores desea ingresar: ")))
    lista =[]
    for i in range(cantidad):
        lista.append(int(input("Ingrese el valor: ")))
    return lista
#Verificar si una palabra contiene la letra x o z
def palabra ():
    palabra = (input("ingrese una palabra: "))
    
    return palabra.count ("x") != 0 or palabra.count ("z") != 0
    
continuar="si"
menu_tuplas = ("primo","par","media","palabra")

while continuar=="si":
    operacion=str(input("ingresa el proceso que deseas realizar (primo) (par) (media) (palabra)"))
    if operacion== menu_tuplas[0]:
        print(primo(int(input("Ingrese el número: "))))
    elif operacion== menu_tuplas[1]:
        print(par(int(input("Ingrese el número: "))))
    elif operacion== menu_tuplas[2]:
        print(media(generar_lista()))
    elif operacion== menu_tuplas[3]:
        print(palabra())
    else:   
       print("ingreso una operacion no valida")
    continuar=str(input("Deseas repetir el proceso? Ingresa (no) para cerrar el ciclo y (si) para repetir el proceso "))
