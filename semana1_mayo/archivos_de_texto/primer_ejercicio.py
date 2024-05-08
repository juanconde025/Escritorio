import json
ingreso_empleados = {"Nombre":"","Hora":"","estado":""}

with open("ingreso.json") as informacion:
  persona = json.load(informacion)
  print(persona)

  ingreso = json.dumps(ingreso_empleados)
  file = open("ingreso.json","w")
  file.write(ingreso)