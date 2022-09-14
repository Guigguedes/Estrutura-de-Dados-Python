def funcao():
    lista = [2,3,6,19,2,45,34,12,-34]
    maior = max(lista)
    print(maior)

    soma = sum(lista)
    print(soma)

    x = lista[0]
    ocorrencias = lista.count(x)
    print(ocorrencias)

    media = sum(lista) / len(lista)
    print(media)

    somaNegativa = 0 - sum(lista)
    print(somaNegativa)

funcao()