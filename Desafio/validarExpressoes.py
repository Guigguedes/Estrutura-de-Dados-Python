#Feito por: Gabriela Giolo e Guilherme Guedes

from pilhas import Pilha

if __name__ == '__main__':
    expr = input('Digite a expressão: ')
    expr = list(expr)

    p = Pilha()

    simb_abertura = ['{', '[', '(']
    simb_fechamento = ['}', ']', ')']

    for ch in expr:
        if ch in simb_abertura:
            p.push(ch)
            continue

        if ch in simb_fechamento:
            indice_simbolo = simb_fechamento.index(ch)

            if indice_simbolo != -1 and p.peek() == simb_abertura[indice_simbolo]:
                p.pop()
            else:
                print('Expressão inválida')
                break

    if len(p) > 0:
        print('Expressão inválida')
    else:
        print('Expressão válida')