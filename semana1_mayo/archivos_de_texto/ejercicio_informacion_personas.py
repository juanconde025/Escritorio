personas = [{"Nombre": "Pedro","Edad": 54, "Hoobie": "Correr"}]

with open("archivo.txt","a")as file:
    for i in personas:
        file.write(i["Nombre"]+","+str(i["Edad"])+","+i["Hoobie"]+"\n")
