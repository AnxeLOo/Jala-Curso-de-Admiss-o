import os

class CustomList:
    def __init__(self, items):
        self.lista = items
    
    def get(self, index):
        if index > len(self.lista):
            return 'O índice que você está lidando para inserir não está na lista'
        else:
            return self.lista[index]

lista_numeros = [1, 3, 4 ,5 ,6 ,7]

for i, numero in enumerate(lista_numeros):
    print(i, ' - ',numero)

while True:
    entrada = input('Digite o indice desejado: ')
    if entrada.isdigit():
        entrada = int(entrada)
        break
    else:
        os.system('cls')
        print('Por favor digite APENAS numeros!')
        continue

custom_list = CustomList(lista_numeros)

print(custom_list.get(entrada))