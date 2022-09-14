import csv
import os
from tkinter.messagebox import showerror

periodicTable = {}
states = {'l': 'Líquido', 'g': 'Gasoso', 's': 'Sólido'}
table = {}


archive = csv.reader(open('elementos.txt'), delimiter=';')
for i, line_data in enumerate(archive):
    if i == 0:
        continue

    data = {}
    data['simbolo'] = line_data[0]
    data['nome'] = line_data[1]
    data['atomico'] = line_data[2]
    data['linha'] = line_data[3]
    data['coluna'] = line_data[4]
    data['estado'] = line_data[5]

    table[i] = data
    periodicTable[data['simbolo']] = data
    periodicTable[data['nome']] = data
    periodicTable[data['atomico']] = data
    periodicTable[data['linha']] = data
    periodicTable[data['coluna']] = data
    periodicTable[data['estado']] = data


def answerValidation():
    if correctAnswer == True:
        showElement()
    else:
        print('Elemento Inválido.')


def elementValidation():
    if correctAnswer == True:
        data = input('Qual dado deseja exibir?\n')
        if data == 'simbolo':
            os.system('cls')
            print("Simbolo:", periodicTable[element]["simbolo"])
        elif data == 'nome':
            os.system('cls')
            print("Nome:", periodicTable[element]["nome"])
        elif data == 'atomico':
            os.system('cls')
            print("Atômico:", periodicTable[element]["atomico"])
        elif data == 'linha':
            os.system('cls')
            print("Linha:", periodicTable[element]["linha"])
        elif data == 'coluna':
            os.system('cls')
            print("Coluna:", periodicTable[element]["coluna"])
        elif data == 'estado':
            os.system('cls')
            print("Estado:", states[periodicTable[element]["estado"]])
        else:
            print('Dado selecionado é inválido.')
    else:
        ('Esse elemento não existe.')


def showElement():
    simbolo = periodicTable[element]["simbolo"]
    nome = periodicTable[element]["nome"]
    atomico = periodicTable[element]["atomico"]
    linha = periodicTable[element]["linha"]
    coluna = periodicTable[element]["coluna"]
    estado = states[periodicTable[element]["estado"]]

    print(f"""
{nome:=^40}
Simbolo: {simbolo}
Atômico: {atomico}
Linha: {linha}
Coluna: {coluna}
Estado: {estado}
{'='*40}
""")


option = int(input('''
O que você quer?
[1] Ver todos os Elementos.
[2] Buscar por um elemento e ver seus dados.
[3] Bucar com um elemento e ver um dado específico.\n'''))

if option == 1:
    os.system('cls')
    elementTable = ", ".join([str(_) for _ in periodicTable])
    elementTableList = list(elementTable.split(', '))
    for element in elementTableList:
        showElement()
        
elif option == 2:
    elementTable = ", ".join([str(_) for _ in periodicTable])
    elementTableList = list(elementTable.split(', '))
    element = input('Qual elemento?\n')
    for i in elementTableList:
        if element == i:
            os.system('cls')
            correctAnswer = True
            answerValidation()
            break
        else:
            os.system('cls')
            correctAnswer = False
            answerValidation()
            break

elif option == 3:
    elementTable = ", ".join([str(_) for _ in periodicTable])
    elementTableList = list(elementTable.split(', '))
    element = input('Qual elemento?\n')
    for i in elementTableList:
        if element == i:
            correctAnswer = True
            os.system('cls')
            elementValidation()
            break
        else:
            correctAnswer = False
            os.system('cls')
            elementValidation()
            break
else:
    print('Essa opção não é válida...')