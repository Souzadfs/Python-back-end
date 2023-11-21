# Iterável -> str, range, etc ( __iter__)
# iterador -> quem sabe entregar um valor por vez
# next -> me entregue o proximo Valor 
# iter -> me entregue seu iterador

texto = ('Luiz')
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break    