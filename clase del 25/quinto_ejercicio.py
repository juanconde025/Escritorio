print("Ingresa tu nombre y genero")
nombre = input()
sexo = input()

if sexo == "masculino" and nombre[0] <= "m":
  print("su grupo es el B")
elif sexo == "masculino" and nombre[0] >= "n":
  print("su grupo es el A")
elif sexo == "femenino" and nombre[0] >= "n":
  print("su grupo es el B")
elif sexo == "femenino" and nombre[0] <= "m":
  print("su grupo es el A")