inicio = input("Para ingresar el juego ingresa 1: ")

while inicio == "1":
   print("Bienvenidos: al juego de encadenamiento de animales, este juego consiste en que con la primera palabra arroje el programa debe ingresar otra pablra que inicie con la letra que finalizo la anterior palabra (OJO: Las pablras a ingresar son de acuerdo a la tematica: Animales) debes intentar adivinar los animales los cuales estan guardados en una lista, si lo haces te felicitara, de lo contrario no. Durante el juego puedes indicar si deseas continuar o salir")
   palabras_tematica = ["Oso","Aguila","Camaleon","Abeja","Serpiente","Hormiga","Perro","Gato","Pez","Cocodrilo","Avestruz","Obeja","Canario","Raton","Iguana","Anguila","Avispa","Ornitorrinco","Elefante"]
   primera_palabra = palabras_tematica[12]
   print(f"El primer animal es: {primera_palabra} " )

   while(inicio == "1"):

   

    animal = input("El usuario debe adivinar: ")
    if animal in palabras_tematica:
    
      print("Has acertado el animal correctamente")
  
    else:
     print("No has acertado el animal correctamente")

    continuar = input("Si deseas continuar ingresa (1), si deseas salir ingresa (2)")
  
    if continuar == "1":
     print("CONTINUEMOS")

    elif continuar == "2":
     break
 
    else:
      print("Debe ingresar 1 o 2")   

   if continuar == "2":
     break
   
   