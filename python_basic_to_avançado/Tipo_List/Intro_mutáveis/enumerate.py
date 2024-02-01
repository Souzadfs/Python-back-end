lista = ['Maria', 'Denis', 'Lara', 'Analice', 'Debora']

lista_enumerate = enumerate(lista)
lista.append('João')

for item in lista_enumerate:
    print(item)
