entrada = input("Digite um número: ")

if entrada.isdigit():
    numero = int(entrada)

    if numero % 2 == 0:
        print(f"O número que você digitou {numero} é PAR !!!")
    else:
        print(f"O número que você digitou {numero} é ÍMPAR !!!")
else:
    print(f"Você digitou {entrada} e isso não é um número.")
