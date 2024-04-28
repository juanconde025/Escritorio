def mcd(num1, num2):
    
    while num2 > 0:
        
        resto = num1 % num2 
        

        if resto == 0:
            resultado = num2
            
            break


        nuevo_divisor = num1 % resto
        if nuevo_divisor == 0:
            resultado = resto
            break           

    return  resultado

def mcm(num1, num2):
    resultado = (num1 *num2) // mcd(num1, num2)
    return resultado



decision = input("Ingresa (1) para realizar el maximo comun divisor o ingresa (2) para realizar el minimo comun multiplo ")

while (True):
    if decision == "1":
        num1 = int(input("Ingresa el numero mayor "))
        num2 = int(input("Ingresa el numero menor "))
        resultado = mcd(num1, num2)
        print(f"El MCD es ", resultado)


    elif decision == "2":
        num1 = int(input("Ingresa el primer numero "))
        num2 = int(input("Ingresa el segundo numero "))
        resultado = mcm(num1, num2)
        print(f"El MCM es ", resultado)
    else:
        print("Debes ingresar un numero entre 1 y 2")

    if decision == 1 or 2:
        break
