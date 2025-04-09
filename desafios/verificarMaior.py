def verificar():
    num = int(input("escolha o primeiro numero"))
    num2 = int(input("escolha o segundo numero"))
    if(num > num2):
        print(f"o primeiro numero é maior: {num}")
    elif(num < num2):
        print(f"o segundo numero é maior {num2}")
    else:
        print("os caras são iguais")

verificar()