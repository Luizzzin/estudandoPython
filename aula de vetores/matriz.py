tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

tabuleiro[0][0] = "X"
tabuleiro[1][1] = "0"
tabuleiro[2][2] = "X"

for linha in tabuleiro:
    print(" | ".join(linha))
