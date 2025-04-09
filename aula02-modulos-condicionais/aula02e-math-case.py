escolha_usuario = int(input("escolha um numero"))

match escolha_usuario:
    case 0:
        status = "sair do programa"
    case 1:
        status = "entrar no software"
    case _:
        status = "erro"

print(status)
