asignaturas = ["Matematicas","Lengua","Ingles","Deportes","Quimica"]
notas = []
print(asignaturas)

for i in range(len(asignaturas)):
 nota = float(input("ingrese la nota que saco en "+ asignaturas[i] + " :"))
 notas.append(nota) 
print("")
for i in range(len(asignaturas)):
 print(f"la nota de la asignatura {asignaturas[i]} es {notas[i]} ") 