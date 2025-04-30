lista = ["luiz", "henrique", "barbosa", "dias"]

for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        print(lista[i], lista[j])

