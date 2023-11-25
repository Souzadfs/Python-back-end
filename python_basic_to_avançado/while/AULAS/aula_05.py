frase = 'O python é uma linguagem de programção' \
'multiparadigma'\
'Python foi criado por Guido Van Rossum.'

i =0

while i < len(frase):
    letra_atual = frase[i]
    qts_vezes_aparece_letras = frase.count(letra_atual)

    print(letra_atual, qts_vezes_aparece_letras)

    i += 1