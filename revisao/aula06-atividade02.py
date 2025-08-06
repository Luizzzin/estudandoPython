linha = 4
colunas = 5

matriz = []

numero = 1

for i in range(linha):
    lin = []
    for j in range(colunas):
        lin.append(numero)
        numero += 1
    matriz.append(lin)

for lin in matriz:
    print(lin)