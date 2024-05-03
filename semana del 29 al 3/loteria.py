
lista_premios = {"un carro","un celular","una moto"}
balotas = {"1","2","3","4","5"}


print ("LOTERIA: ingrese un numero de uno a cinco para asignarle dicho numero")


while balotas:
 
 choice = input("ingrese el num de 1 a 5: ")
 boleta_ganadora = balotas.choice()
 premio = lista_premios.choice()

 if choice == boleta_ganadora:

    print(f"se elimina el num {choice}")
    print(f"gano {premio}" )
    break

 elif choice in balotas:

    num_eliminado = balotas.remove(choice)
    print(f"se elimina el num {choice}")
    print("no gano")
    
 
 elif choice not in balotas:
    print("ta mal")
    break
 



    