import random
vetUF = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", 
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", 
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", 
    "São Paulo", "Sergipe", "Tocantins"
]
vetES = [random.randint(1, 500) for _ in range(27)]
def media_geometrica(lista):
    produto = 1
    for valor in lista:
        produto *= valor
    return produto**(1 / len(lista))

def media_aritmetica(x):
    N = len(x)
    soma = 0
    for xi in x:
        soma = soma+xi
    media = soma/N
    return(media)
def media_harmonica(lista):
    soma_inversos = 0
    for valor in lista:
        soma_inversos += 1 / valor
    return len(lista) / soma_inversos
    
def desvio_padrao(lista):
    media = media_aritmetica(lista)
    soma_quadrados = 0
    for valor in lista:
        soma_quadrados += (valor - media)**2
    return (soma_quadrados / (len(lista) - 1)) ** 0.5

for i in range (0,len(vetUF)):
  print(vetUF[i],"\t", end="")
  print(vetES[i])

print("=============media aritimetica==========")

print(f"{media_aritmetica(vetES):.2f}")

print("=========================================")

print("=============media geomettrica==========")

print(f"{media_geometrica(vetES):.2f}")

print("=========================================")

print("=============media harmonica==========")

print(f"{media_harmonica(vetES):.2f}")

print("=========================================")

print("=============desvio padrao==========")

print(f"{desvio_padrao(vetES):.2f}")

print("=========================================")
n = len(vetES)
for i in range(n):
  for j in range(0, n-i-1):
    if vetES[j] > vetES[j+1]:
      vetES[j], vetES[j+1] = vetES[j+1],vetES[j]
      vetUF[j],vetUF[j+1]=vetUF[j+1],vetUF[j]
for i in range (0,len(vetUF)):
  print(vetUF[i],"\t", end="")
  print(vetES[i])