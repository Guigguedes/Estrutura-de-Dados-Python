import os
class Fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)

    def front(self): # mostrar o 1o da fila, sem remover!
        return self._vet[0]
        
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)


if __name__ == "__main__":
    f1 = Fila()
num = list()
cont = 0
print('-=' *50)
while True:
    print('''
                                                          MENU
                    
                         [1] Obeter nova senha   [2]Chamar proxima senha    [3]Mostrar senhas chamadas      
        
[5] Para sair 
        ''')

    escolha = int(input('Escolha uma opção: '))
    os.system('cls')
    if escolha == 1:
        f1.enqueue(cont)
        cont = cont + 1
    elif escolha == 2:
        if f1.is_empty():
            print('Primeiro obtenha uma senha!! -Digite o numero [1]')
        else:
            senha = f1.front()
            num.append(senha)
            f1.dequeue()
            print('PROXIMA SENHA:  ', senha)
    elif escolha == 3:
        if len(num) == 0:
            print('Nenhuma senha chamada :/')
        else:
            print('''Ultimas senhas chamadas >>>''', num)
    elif escolha == 5:
        print('''
        
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                      Muito obrigado!! >>>>VOLTE SEMPRE<<<<
                -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-      
                      ''')
        break