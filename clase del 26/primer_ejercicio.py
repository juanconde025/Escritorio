def factorial(num):
    
    for i in range(num,1,-1):
      num1 = num1 * i
      
    print(num)
    return num1

    


print("ingresa un numero para aplicarle su factorial")
num =int(input())

factorial(num)

