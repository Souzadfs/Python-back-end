palavra_secr = 'perfume'
letras_corretas = ''
while True:
    letra = input('Digite uma letra: ')
   
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