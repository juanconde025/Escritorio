print("Para la frase (bienvenidos campers) se le leera al reves, el caracter de la tercera posicion, separa con comas, los une con guion y demas funciones")
mi_cadena = ("bienvenidos, campers")
mi_subcadena = mi_cadena[::-1]
print(mi_subcadena)
cadena_leer3pos = mi_cadena[2]
print(cadena_leer3pos)
separar = mi_cadena.split(",")
print(separar)
unir = "-".join(separar)
print(unir)
mayuscula = mi_cadena.upper ()
minuscula = mi_cadena.lower ()
primeraMayuscula = mi_cadena.capitalize ()
titulada = mi_cadena.title ()
print(mayuscula)
print(minuscula)
print(primeraMayuscula)
print(titulada)



indice = mi_cadena.find("campers")
cambio = mi_cadena.replace("bienvenidos","Welcome")
print(indice)
print(cambio)