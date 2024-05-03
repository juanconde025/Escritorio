mercado = {
    "Menta": 300,
    "Chocorramo": 1000,
    "Esfero": 2700,
    "Chocolatina": 2500
}

opcion = input("Que producto desea: ")
while (True):
 if opcion == "Menta":
    print(mercado.get("Menta"))
    break
 elif opcion == "Chocorramo":
    print(mercado.get("Chocorramo"))
    break
 elif opcion == "Esfero":
    print(mercado.get("Esfero"))
    break
 elif opcion == "Chocolatina":
    print(mercado.get("Chocolatina"))
    break
 elif opcion not in mercado:
    print("no es una opcion valida")
    break