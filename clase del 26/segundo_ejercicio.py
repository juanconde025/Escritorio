def iva_cobro(sin_iva, valor_iva=0.21):
  total2 = float((sin_iva * valor_iva) + sin_iva)
  
  return print (f"tu valor total es ", total2)



sin_iva = int(input("ingresa el valor sin iva "))
opcion = int(input("si desea aplicar iva presione 1, si desea aplicar el iva por defecto (21%) presione 2 "))
if opcion == 1:
    valor_iva = float(input("que valor desea agregar como iva? ingreselo como decimal "))
    while (True):
     if valor_iva < 0:
       valor_iva = float(input("debes ingresar un valor flotante positivo "))
     else: 
      total1 = (iva_cobro(sin_iva, valor_iva))
     break
elif opcion == 2:
  total2 = iva_cobro(sin_iva)
  
  
