print("ingresa tu edad y tus ingresos en euros")

edad = int(input())
ingresos = int(input())

if edad >= 16 and ingresos >= 1000:
    print("debes tributar")

else: print("no debes tributar")