matriz = [[0, 0], [0, 0]]
r= [[0, 0], [0, 0]]
for l in range(0, 2):
    for c in range(0, 2):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]  : '))

maior = -1
for l in range(2):
    for c in range(2):
      if matriz[l][c] > maior:
       maior = matriz[l][c]
       
for l in range (2):
  for c in range (2):
    r[l][c] = matriz[l][c] *maior
    print (r)