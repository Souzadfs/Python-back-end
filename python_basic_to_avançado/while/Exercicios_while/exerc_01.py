while True:
    num_1 = input("Digite um número")
    num_2 = input("Digite outro número")
    operador = input( "Digite o operador ( + - / * ) ") 
    
    num_validos = None
    number_1 = 0
    number_2 = 0

    try:
        number_1 = float(num_1)
        number_2 = float(num_2)
        num_validos = True
    except:
        num_validos = None 

    if num_validos is None:
        print(" Um ou ambos são inválidos. ")       
        continue

    operadores_permitidos = ' +-/* ' 
    if operadores_permitidos not in operador:
        print(' Operador inválido')
        continue
    if len(operador) > 1:
        print('Você precisa digitar apenas um operador')
        continue
    if operador == '*':
        print(number_1 * number_2)
    elif operador == '-':
        print(number_1 - number_2)

    elif operador == '+':
        print(number_1 + number_2)

    elif operador == '/':
        print(number_1 / number_2)
    
    sair = input('Quer sair do programa? [s]im').lower().startswith('s') 