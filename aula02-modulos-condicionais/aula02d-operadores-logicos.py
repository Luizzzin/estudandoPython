#logica e (and)
verifica_email = True
verifica_senha = True

verifica_login =  verifica_email and verifica_senha
print(verifica_login)

if verifica_email and  verifica_senha:
    print("deixa o cara")

if not verifica_login:
    print("loga ai direito")