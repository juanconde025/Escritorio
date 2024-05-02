import random


words_list = ["perros", "gato", "casa", "mesa", "silla", "libro", "arbol", "osa", "sol", "luna"]


print("¡Bienvenido al juego de encadenamiento de palabras! este juego consiste en que con la primera palabra arroje el programa debe ingresar otra pablra que inicie con la letra que finalizo la anterior palabra (OJO: Las pablras a ingresar son de acuerdo a la tematica: Animales) debes intentar adivinar los animales los cuales estan guardados en una lista, si lo haces te felicitara, de lo contrario no. Durante el juego puedes indicar si deseas continuar o salir")

current_word = random.choice(words_list)
last_letter = current_word[-1]
print(f"La primera palabra es: {current_word}")

while True:
    
    player_input = input("Jugador 1, ingresa una palabra: ")

    if player_input == "salir":
    
        print("¡Gracias por jugar!")
        break

    elif player_input not in words_list or player_input[0] != last_letter:
    
        print("Palabra no válida. Inténtalo de nuevo.")
        

    elif player_input in words_list and player_input[0] == last_letter:
    
        print("Palabra valida")
        
    last_letter = player_input[-1]
    current_word = player_input
    print(f"Jugador 1: {current_word}")


    player_input = input("Jugador 2, ingresa una palabra: ")

    if player_input == "salir":
    
        print("¡Gracias por jugar!")
        break
    
    elif player_input not in words_list or player_input[0] != last_letter:
        
        print("Palabra no válida. Inténtalo de nuevo.")
        

    elif player_input in words_list and player_input[0] == last_letter:
    
        print("Palabra valida")
        
    last_letter = player_input[-1]
    current_word = player_input
    print(f"Jugador 2: {current_word}")