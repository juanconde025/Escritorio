from informacion_empresas import Empresas

while(True):
 print("Bienvenido al menu de informacion de empresas\n Para mostrar cuantas empresas tienen más de 10 empleados en Recursos Humanos, presione 1\n Para mostrar el promedio de empleados por departamento presione 2\n Para mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas presione 3\n para mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas sino por departamento presione 4\n y para salir ingresa 5.")
 option = input()
 if option == "1":
    for llave, valor in Empresas.items(): 
        if valor[0]["empleados"] > 10:
            print(llave)
            print (f"Tiene ",  valor[0]["empleados"], " empleados")
 elif option == "2":
    contador = 0
    dividendo = 0
    for llave, valor in Empresas.items():  
         dividendo += 1
         for k in valor:
            if k["departamento"] == "Recursos Humanos":
              valores = (k["empleados"])
              contador += valores 
   
    
    promedio = contador // dividendo
    print(promedio)

 elif option == "3": 
    for llave, valor in Empresas.items():
        if valor[3]["empleados"] > valor[2]["empleados"]:
            valor[2]["empleados"] = valor[2]["empleados"] * 2
            if valor[3]["empleados"] > valor[2]["empleados"]:
                print(f"La {llave} tiene el doble o mas empleados en operaciones que en ventas")
 elif option == "4":
    
    del Empresas["Empresa 1"]
    Empresas["departamento_RH"] = [{"empleados":48}]
  
    del Empresas["Empresa 2"]
    Empresas["departamento_Contabilidad"] = [{"empleados":82}]

    del Empresas["Empresa 3"]
    Empresas["departamento_Ventas"] = [{"empleados":140}]

    del Empresas["Empresa 4"]
    Empresas["departamento_Operaciones"] = [{"empleados":248}]

    del Empresas["Empresa 5"]

    print(Empresas)
 
 if option == "5":
    print("Fin del menu")
    break
 elif option != "1"or"2"or"3"or"4"or"5":
    print("Ingrese un numero entre 1 y 5")