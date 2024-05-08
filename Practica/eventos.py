def registrar_evento(datos):
    datos = dict(datos)
    evento={}
    evento["nombre"]=input("Ingrese el nombre del evento: ")
    evento["locacion"]=input("Ingrese la locacion: ")
    evento["dia"]=input("Ingrese el dia del mes de Agosto: ")
    evento["realizado"]=input("Ingrese 1 si ya se ha realizado, o ingrese 2 si no se ha realizado(si ingresa cualquier otro digito se tomara como no hecho): ")

    if evento["realizado"] == "1":
        evento["realizado"] = True
    elif evento["realizado"] == "2":
        evento["realizado"] = False
    else:
        evento["realizado"] = False
    
    datos["eventos"].append(evento)
    print("Evento registrado!!") 
    
    return datos    
    