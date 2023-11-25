# frase = 'O python é uma linguagem de programção' \
# 'multiparadigma'\
# 'Python foi criado por Guido Van Rossum.'

# i =0

# while i < len(frase):
#     letra_atual = frase[i]
#     qts_vezes_aparece_letras = frase.count(letra_atual)

#     print(letra_atual, qts_vezes_aparece_letras)

#     i += 1

frase = 'Um texto é uma manifestação da linguagem. Pode ser definido como tudo aquilo que é dito por'\
      'um emissor e interpretado por um receptor. Dessa forma, tudo que é interpretável é um texto. Outra forma de''\
        conceituação é pensar que tudo aquilo que produz um sentido completo'\
    'que seja uma mensagem compreensível, é um texto..'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)