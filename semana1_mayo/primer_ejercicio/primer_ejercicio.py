from informacion_empresas import Empresas

print("Bienvenido al menu de informacion de empresas\n Para mostrar cuantas empresas tienen más de 10 empleados en Recursos Humanos, presione 1\n Para mostrar el promedio de empleados por departamento presione 2\n Para mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas presione 3\n Y para mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas sino por departamento presione 4.")
option = input()

if option == "1":
    for llave, valor in Empresas.items(): 
        if valor[0]["empleados"] > 10:
            print(llave)
            print (f"Tiene ",  valor[0]["empleados"], " empleados")



