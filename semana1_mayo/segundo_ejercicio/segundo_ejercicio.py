

def numeros_perfectos(numero):
 
 
 suma_divisores = 0

 for i in range(1, numero):
     if numero % i == 0:
         suma_divisores += i

 if suma_divisores == numero:
        numeros_perfectos_encontrados.append(numero)

 
 return numeros_perfectos_encontrados

from import_ejercicio2 import numeros_perfectos_encontrados
numero = 2

while len(numeros_perfectos_encontrados) < 4:
 numero += 1 
 result = numeros_perfectos(numero)
  
 print("Los primeros 4 números perfectos son:")
 print(result)
 break