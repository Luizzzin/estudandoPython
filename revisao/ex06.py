import random

n = 0
while n <= 0 :
    n = int(input("Digite um numero inteiro positivo\n"))

vetor = []

for i in range(n):
    num_aletorio = random.uniform(0, 100)
    vetor.append(num_aletorio)
print(vetor)