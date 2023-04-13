import random
import os

class game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.jogadas = {'tesoura': ('papel','largato'),
           'papel': ('pedra','spock'),
           'pedra': ('tesoura','largarto'),
           'largato': ('spock','papel'),
           'spock': ('tesoura','pedra')
           }

    def partida(self):

            if self.p1 == self.p2:
                print('Empate')
            elif self.p2 in self.jogadas[self.p1]:
                print('Player 1 venceu')
            else:
                print('Player 2 venceu')
        
validos = ('tesoura', 'papel', 'pedra', 'lagarto', 'spock')

opcoes_maquina = ('s', 'n')
escolher_maquina = ''
maquina = False
maquina_jogada = ''

while escolher_maquina.lower() not in opcoes_maquina:
    os.system('cls')
    escolher_maquina = input('Voce deseja jogar contra a maquina [S] ou [N]? ')

if escolher_maquina.lower() == 's':
    maquina = True

if maquina == True:
    maquina_jogada = random.choice(validos)

player_1 = ''
player_2 = ''

while player_1.lower() not in validos:
    player_1 = input('Escolha uma jogada, player 1: ')

if maquina is not True:
    while player_2.lower() not in validos:
        player_2 = input('Escolha uma jogada, player 2: ')
else:
    player_2 = maquina_jogada

if maquina is True:
    print(f'A maquinha esolheu: {maquina_jogada}')

partida = game(player_1, player_2)
partida.partida()