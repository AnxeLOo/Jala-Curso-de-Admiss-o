class patodeborracha:

    def __init__(self, cor, tamanho, peso):
        self.cor = cor 
        self.tamanho = tamanho
        self.peso = peso
        print(f'Cor: {cor}', \
              f'Tamanho: {tamanho}',\
              f'Peso: {peso}', sep='\n'
              )

    def emitirsom(self):
        pass

    def flutuar(self):
        pass

    def esguichar_agua(self):
        pass

patinho_1 = patodeborracha('Amarelo', 'M', 13)
patinho_1.emitirsom()
patinho_1.flutuar()
patinho_1.esguichar_agua()
print()
patinho_2 = patodeborracha('Verde', 'P', 9)
patinho_2.emitirsom()
patinho_2.flutuar()
patinho_2.esguichar_agua()
print()
patinho_3 = patodeborracha('Cinza', 'G', 15)
patinho_3.emitirsom()
patinho_3.flutuar()
patinho_3.esguichar_agua()