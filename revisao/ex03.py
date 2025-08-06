n = 0
while n <= 0 :
    n = int(input("Digite um numero inteiro positivo"))

soma = 0
for i in range (1, n + 1):
    soma += i

print(f"a soma de 1 ate {n} = {soma}")