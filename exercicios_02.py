nome = input("Como é seu nome? ")
qtd_letras = len(nome)

if qtd_letras < 5:
    print(f" Seu nome é {nome} e tem {qtd_letras} letras e é curto.")
elif qtd_letras < 7:
    print(f"Seu nome é {nome} e tem {qtd_letras} letras e é normal")   
else:
    print(f"Seu nome é {nome} e tem {qtd_letras} letras e é muito grande")    

