
#estrutura condicional simples
# nota = int(input("Qual sua nota?"))
#
# if(nota <= 5):
#     print("nota baixa")
#
# print("fim")
#----------------------------



#estrutura condicional composta
# nota_final = int(input("Qual sua nota?"))
#
# if(nota_final <= 5):
#     print("nota baixa")
# else:
#     print("aprovado")
#
# print("fim")
#-----------------------------------

#estrutura condicional encadeada

# nota_final = int(input("qual a sua nota final?"))
#
# if(nota_final < 4):
#     print("reprovado")
# else:
#     if(nota_final < 6):
#         print("recuperacao")
#     else:
#         print("aprovado")
#---------------------------------

#estrutura condicional composta - elif

nota_final = int(input("qual a nota?"))

if(nota_final < 4):

    print("reprovado")
elif(nota_final < 6):

    print("recuperacao")
else:

    print("aprovado")