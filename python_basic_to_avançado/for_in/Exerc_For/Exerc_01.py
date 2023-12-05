import os

palavra_secr = 'perfume'
letras_corretas = ''
s = 0
while True:
    

    letra = input('Digite uma letra: ')
    s += 1
   
    if len(letra) > 1:
        print('Digite apenas uma letra! ')
        continue

    if letra in palavra_secr:
        letras_corretas += letra
  
    palavra_formada = ''
    for letra_secreta in palavra_secr:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        
        else:
           palavra_formada += '*'
    print(palavra_formada)       

    if palavra_formada == palavra_secr:
        print(f'você Acertou !!!! ')   
        print(f'A palavra secreta é ({palavra_secr})')
        print(f' Suas tentativas foram {s}x')
        s = 10 
        break