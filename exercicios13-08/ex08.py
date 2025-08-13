import random

qtd_lin = int(input("Digite o num de linhas\n"))
qtd_colunas = int(input("Digite o num de colunas\n"))

A = []
B= []
C = []

for i in range(qtd_lin):
    linha_A = []
    linha_B = []
    for j in range(qtd_colunas):
        valor_A = random.randint(-10, 10)
        linha_A.append(valor_A)

        valor_B = random.randint(-10, 10)
        linha_B.append(valor_A)

        A.append(linha_A)
        B.append(linha_B)

for linha in A:

    print(linha)
print("==========")
for linha in B:

    print(linha)

for i in range(qtd_lin):
    linha_soma = []
    for j in range(qtd_colunas):
        valor_soma = A[i][j] + B[i][j]
        linha_soma.append(valor_soma)
    C.append(linha_soma)
print("==========")
for linha in C:
    print(linha)