def obtener_muestra_numerica():
  """
  Solicita al usuario una muestra de números separados por comas y los devuelve como lista.

  Returns:
    Una lista con los números ingresados.
  """
  muestra_texto = input("Ingrese una muestra de números separados por comas: ")

  # Dividir la cadena de texto en una lista de números
  numeros_texto = muestra_texto.split(",")

  # Convertir los números de texto a números flotantes
  numeros = []
  for numero_texto in numeros_texto:
    try:
      numero = float(numero_texto)
      numeros.append(numero)
    except ValueError:
      print(f"Error: '{numero_texto}' no es un número válido. Se omitirá.")

  return numeros

def calcular_media(numeros):
  """
  Calcula la media de una lista de números.

  Args:
    numeros: La lista de números para calcular la media.

  Returns:
    La media de los números.
  """
  if not numeros:
    raise ValueError("No se proporcionaron números para calcular la media.")

  suma = 0
  for numero in numeros:
    suma += numero

  return suma / len(numeros)

def main():
  """Función principal del programa."""
  numeros = obtener_muestra_numerica()

  try:
    media = calcular_media(numeros)
    print(f"La media de la muestra es: {media:.2f}")
  except ValueError as error:
    print(f"Error: {error}")

if __name__ == "__main__":
  main()
