import os

class WeatherMachine:
    def __init__(self, name):
        self.nome = name
    
    def converter_temp(self, celcius):
        self.fahrenheit = (celcius * 1.8) + 32
        return self.fahrenheit

    def get_weather(self, temperature):
        print(f'{temperature: .1f}F°')
        if temperature >= 65:
            print(f'{self.nome} clima é ideal para sair sem casaco')
        else:
            print(f'{self.nome} fique em casa, está frio lá fora')

usuario = input('Digite seu nome: ')

opcoes_SimNao = ('s', 'n')
check_temp = ''

while check_temp.lower() not in opcoes_SimNao:
    check_temp = input('A temperatura que sera informada esta Celcius [S] ou [N]? ')

entrada_temp = ''
while True:
    entrada_temp = input('Qual a temperatura? ')
    try:
        temp_int = int(entrada_temp)
        os.system('cls')
        break
    except ValueError:
        continue

weather_machine = WeatherMachine(usuario)
if check_temp.lower() == 's':
    weather_machine.get_weather(weather_machine.converter_temp(temp_int))
else:
    weather_machine.get_weather(temp_int)