print("Aqui iremos verificar os numeros primos de 2 ate 2000, >:3")
#protipo

for numero in range(2, 2001):
    primo = True
    for div in range(2, numero):
        if numero % div == 0:
            primo = False
            break

    if primo:
        print(numero)

