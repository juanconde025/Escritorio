abecedario =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
elim = []

for i in range(len(abecedario)):
  if i % 3 == 0:
    elim.append(i)

for i in elim:
  print(abecedario[i])
  