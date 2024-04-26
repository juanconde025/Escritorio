def clasificar_alumno(nombre, sexo):
  return grupo
  
  """


  Esta función clasifica a un alumno en el grupo A o B según su sexo y nombre.

  Args:
    nombre: El nombre del alumno (string).
    sexo: El sexo del alumno ("M" para masculino, "F" para femenino).

  Returns:
    El grupo al que pertenece el alumno ("A" o "B").
  """
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ").upper()

if sexo == "F" and nombre[0] < "M":
    grupo = "A"
elif sexo == "M" and nombre[0] > "N":
    grupo = "A"
else:
    grupo = "B"
    


# Solicitar el nombre y sexo al usuario


# Clasificar al alumno
grupo = clasificar_alumno(nombre, sexo)

# Mostrar el grupo al que pertenece el alumno
print(f"Usted pertenece al grupo {grupo}.")
