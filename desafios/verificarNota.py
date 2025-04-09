def adicionarNota():
    nota1 = int(input("qual a primeira nota?"))
    nota2 = int(input("Qual a segunda nota?"))
    nota3 = int(input("Qual a terceira nota?"))
    nota4 = int(input("Qual a quarta nota?"))
    soma = (nota1 + nota2 + nota3 + nota4)
    div = soma / 4
    if (div >= 7):
        print(f"{div}passou de ano")
    elif (div >= 5):
        print(f"foi {div}recuperação")
    else:
        print(f" {div}ahahahaha")


adicionarNota()