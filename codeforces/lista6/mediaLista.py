def media_lista(lista):

    soma = sum(lista)
    tamanho = len(lista)

    return int(soma/tamanho)

print(media_lista([5, 1, 2, 3, 4, 5]))