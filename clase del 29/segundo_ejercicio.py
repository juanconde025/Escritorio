asignaturas = ["Matematicas","Lengua","Ingles","Deportes","Quimica"]
materia = input("Ingresa con que materia quieres mostrar el siguiente mensaje (Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista)").capitalize()

if materia == asignaturas[0]:
    print("Yo estudio "+ asignaturas[0] + " donde "+ asignaturas[0] +" esta en la primera posicion")
elif materia == asignaturas[1]:
    print("Yo estudio "+ asignaturas[1] + " donde "+ asignaturas[1] +" esta en la segunda posicion"  )
elif materia == asignaturas[2]:
    print("Yo estudio "+ asignaturas[2] + " donde "+ asignaturas[2] +" esta en la tercera posicion" )
elif materia == asignaturas[3]:
    print("Yo estudio "+ asignaturas[3] + " donde "+ asignaturas[3] +" esta en la cuarta posicion" )
elif materia == asignaturas[4]:
    print("Yo estudio "+ asignaturas[4] + " donde "+ asignaturas[4] +" esta en la quinta posicion" )
 