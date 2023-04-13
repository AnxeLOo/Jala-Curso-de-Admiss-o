class CustomList:
    def __init__(self, items):
        self.items = items
    
    def delete(self, value):
        if value in self.items:
            self.i = self.items.index(value)
            del self.items[self.i]
            print(*self.items, sep=' - ')
        else:
            print('O valor nao esta na lista')

cores = ["green", "blue", "yellow", "brown"]
print(*cores, sep=' - ')

custom_list = CustomList(cores)

entrada = input('Digite uma cor a ser apagada: ').lower()

custom_list.delete(entrada)