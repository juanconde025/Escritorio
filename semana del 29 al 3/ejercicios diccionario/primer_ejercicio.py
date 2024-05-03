Divisa = {"Euro":"€","Dolar":"$","Yen":"¥"}
mostrar = Divisa
pregunta = input("Que divisa desea: ").title()
while(True):
 if pregunta == "Euro":
    print("€")
    break
 elif pregunta == "Dolar":
    print("$")
    break
 elif pregunta == "Yen":
    print("$")
    break
 elif pregunta not in Divisa:
    print("tu ta loco busque otra divisa")
    break