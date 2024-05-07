def perfectos():
    numeros_perfectos_encontrados = []
    numero = 2

    while len(numeros_perfectos_encontrados) < 4:
        suma_divisores = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma_divisores += i

        if suma_divisores == numero:
            numeros_perfectos_encontrados.append(numero)

        numero += 1

    print("Los primeros 4 números perfectos son:")
    print(numeros_perfectos_encontrados)


