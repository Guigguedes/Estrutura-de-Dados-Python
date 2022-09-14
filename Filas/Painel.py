from Fila import *
import os
import time


if __name__ == '__main__':
    fila = Fila()
    contador = 0 # contador de clientes
    senhasChamadas = RingBuffer() # lista de senhas chamadas
    senhasChamadas.init(5)

    while True:
        os.system('cls')
        print("""
                                             MENU
        (1) - Obter nova senha
        (2) - Chamar senha 
        (3) - Mostrar senhas chamadas
        (4) - Sair
        """)
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            contador += 1
            fila.enqueue(contador)
            print('Senha %d adicionada com sucesso!' % contador)
            time.sleep(2)

        elif opcao == 2:
            if not fila.is_empty():
                senha = fila.front()
                fila.dequeue()
                senhasChamadas.append(senha)
                print("Senha %d atendida" % senha)
                input('Pressione <ENTER> para continuar...')
            else:
                print("Fila vazia!")

        elif opcao == 3:
            print('''As últimas senhas chamadas foram:''' , senhasChamadas.get())
            input('Pressione <ENTER> para continuar...')

        elif opcao == 4:
            break

        else:
            print('Opcao invalida')
            input('Pressione <ENTER> para continuar...')