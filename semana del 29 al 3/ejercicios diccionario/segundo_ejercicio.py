informacion = {"nombre": "",
   "edad": "",
   "direccion": "",
   "telefono": "",
}

informacion["nombre"] = input("ingrese su nombre: ")
informacion["edad"] = input("ingrese su edad: ")
informacion["direccion"] = input("ingrese su direccion: ")
informacion["telefono"] = input("ingrese su telefono: ")

print(f"su nombre es: ",informacion.get("nombre"), "tiene: ", informacion.get("edad"), " años, su direccion es: ",informacion.get("direccion"), " y su telefono es: ",informacion.get("telefono"))


