def contar_vocales(palabra):
 
  vocales = "aeiou"
  conteo_vocales = {}

  for vocal in vocales:
    conteo_vocales[vocal] = 0

  for letra in palabra.lower():
    if letra in vocales:
      conteo_vocales[letra] += 1

  return conteo_vocales

 
palabra = input("Ingrese una palabra: ")

conteo_vocales = contar_vocales(palabra)

print("Conteo de vocales:")
for vocal, cantidad in conteo_vocales.items():
    print(f"{vocal}: {cantidad}")

