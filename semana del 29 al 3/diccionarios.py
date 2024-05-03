#paises = {"Nombre":"Colombia", "jugadores" :["James","Falcao"]}
#print(paises["jugadores"][1])
#paises["jugadores"][0] = "Cuadrado"
#print(paises["jugadores"][0])

colegio = {
    "Profesores": ["Juan","Pedro","Nicolas"],
    "Salones": ["Sputnik","Apolo","Artemis","Cosmos"],
    "Notas": [1,2,3,4,5],
    "Materias": ["Matematicas","Español","Deportes","Ingles"]
}

opcion = input("Si desea saber que salon,profesor, materias y nota le toco, presione 1: ")

if opcion == "1":
 print (colegio["Salones"],"<-", ["Salones"][0])
 print (colegio["Profesores"],"<-", ["Profesores"][0])
 print (colegio["Materias"],"<-", ["Materias"][0])
 print (colegio["Notas"],"<-", ["Notas"][0])
else:
 print("no sea tonto") 