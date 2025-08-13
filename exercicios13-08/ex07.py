n = 0
temp = 0
while n <=0:
    n = int(input("Digite o numero de posições do vetor"))

vetor = []

print("Digite os caracterres um por vez")
for i in range(n):
    caractere = input(f"posicao {i} ")
    vetor.append(caractere)
    #invertendo as posições das extremidades
for i in range(n//2):
    temp = vetor[i]
    vetor[i] = vetor[n-1-i]
    vetor[n - 1 - i] = temp

print("\nVetor original : ", vetor)
