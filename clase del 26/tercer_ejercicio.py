#ejercicio area circulo y volumen cilindro
def area_circulo(radio):
    area = radio * radio * 3.1416
    return print(f"el area del circulo es ", area)

def volumen_cilindro(altura, area_c):
    volumen = area_c * altura
    return print(f"el volumen del cilindro es ", volumen)


radio = float(input("Ingrese el radio del circulo para calcular el area "))
area_circulo(radio)
area_c = radio* radio * 3.1416
altura = float(input("Ingrese la altura del cilindro para calcular el volumen "))
volumen_cilindro(altura, area_c)


