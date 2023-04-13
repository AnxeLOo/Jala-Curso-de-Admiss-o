import os

class arrow:
    def __init__(self, args):
        self.valor = args
        self.ponto = '* '

    def draw(self):
        for n in range(1, self.valor):
            print(n * self.ponto)

        for n in range(self.valor, 0, -1):
            print(n * self.ponto)

while True:
    colunas = input('Quantas colunas no total? ')
    if colunas.isdigit():
        colunas = int(colunas)
        if colunas <= 25:
            break
        else:
            os.system('cls')
            print('O tamanho maximo e 25')
            continue
    else:
        os.system('cls')
        print('Por favor digite apenas numeros')
        continue

desenho = arrow(colunas)
desenho.draw()



