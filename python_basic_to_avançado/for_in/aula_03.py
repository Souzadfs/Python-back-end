for i in range(10):
    if i == 4:
        print('i é 4, puland')
        continue
    if i == 9:
        print('i é 9, seu else não será executado')    
        break

    for j in range (1, 3):
        print(i,j)

else:
    print('For completo com sucesso')
