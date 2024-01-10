lista = [10, 20, 30, 40]
mudar = lista[2] = 300
lista.append(50)
lista.append(60)
lista.append(70)
lista.append(80)
ultimo_valor = lista.pop(0)
print(lista[2])
print(f'{lista}, Removido, {ultimo_valor}')