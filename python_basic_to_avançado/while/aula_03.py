
contador = 2

while True:
    entrada = input('Digite o valor: ')

    if entrada.isdigit():  # Verifica se a entrada é um número
        contador = float(entrada)
        contador = contador * 10
        print(contador)
    else:
        break  # Encerra o loop se a entrada for uma string

print(f'Você não digitou um número, você digitou {entrada} Acabou !!!')
