n = 0
while n <= 0 :
    n = int(input("Digite um numero inteiro positivo"))

print(f"divisores de {n}")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)