import csv

estados = {'s': 'Sólido', 'g': 'Gasoso', 'l': 'Líquido', 'd': 'Desconhecido'}
tabela_periodica = {}
tabela = {}

arquivo = csv.reader(open('elementos.txt'), delimiter=';')
for tamanho, dado_linha in enumerate(arquivo):
    if tamanho == 0:
        continue #linha 0 = cabeçalho do arquivo

    dados = {}
    dados['simbolo'] = dado_linha[0]
    dados['nome'] = dado_linha[1]
    dados['atomico'] = dado_linha[2]
    dados['linha'] = dado_linha[3]
    dados['coluna'] = dado_linha[4]
    dados['estado'] = dado_linha[5]

    tabela[tamanho] = dados
    tabela_periodica[dados['simbolo']] = dados

#print(tabela_periodica['Hg'])
#print(tabela_periodica['Fe'])

##########

def verificaExistencia():
    if existe == True:
        print(tabela_periodica[elemento])
    
    else:
        print('')


def verificaElemento():
    if existe == True:
        dado = input('Qual dado? ')
        if dado == 'simbolo':
            print(tabela_periodica[elemento]["simbolo"])
        elif dado == 'nome':
            print(tabela_periodica[elemento]["nome"])
        elif dado == 'atomico':
            print(tabela_periodica[elemento]["atomico"])
        elif dado == 'linha':
            print(tabela_periodica[elemento]["linha"])
        elif dado == 'coluna':
            print(tabela_periodica[elemento]["coluna"])
        elif dado == 'estado':
            print(tabela_periodica[elemento]["estado"])
            print(estados[tabela_periodica[i]["estado"]])
        else:
            print('Esse tipo de dado não existe.')
    else:
        ('Não temos esse elemento na nossa base de dados.')

##########

resposta = input('Digite: \n A => listar todos os elementos \n B => procurar um elemento e listar tudo sobre ele \n C => buscar por um elemento e escolher a informação que deseja \n O que você deseja? ').upper()

if resposta == 'A':
    print(tabela_periodica)

elif resposta == 'B':
    tabela_elementos = ", ".join([str(_) for _ in tabela_periodica])
    tabela_elementos_list = list(tabela_elementos.split(', '))
    elemento = input('Qual é o elemento? ').title()
    for i in tabela_elementos_list:
        if elemento == i:
            existe = True
            verificaExistencia()
        else:
            existe = False
            verificaExistencia()

elif resposta == 'C':
    tabela_elementos = ", ".join([str(_) for _ in tabela_periodica])
    tabela_elementos_list = list(tabela_elementos.split(', '))
    elemento = input('Qual elemento? ').title()
    for i in tabela_elementos_list:
        if elemento == i:
            existe = True
            verificaElemento()
        else:
            existe = False
            verificaElemento()
            
else:
    print('Essa opção não é válida.')

