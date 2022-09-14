#Feito por: Gabriela Giolo e Guilherme Guedes

from pilhas import Pilha

def dec2bin(decimal):
    p1 = Pilha()
    while decimal > 0:
        resto = decimal % 2
        p1.push(resto)
        decimal = decimal // 2
    while len(p1) > 0:
        print(p1.pop(), end='')

decimal = int(input("Digite um número inteiro: "))
dec2bin(decimal)
