asignaturas = ["Matematicas", "Sociales", "Ingles", "Fisica", "Quimica"]
notas = []


for i in range(len(asignaturas)):
 nota = float(input(f"Ingrese la nota de la materia {asignaturas[i]} :"))

 if nota < 3:
  notas.append(i) 

print("Debe repetir:")
for i in notas:
 print(asignaturas[i]) 