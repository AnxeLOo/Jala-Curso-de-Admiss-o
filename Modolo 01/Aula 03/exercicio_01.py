import os

while True:    

    entrada = input('Digite um numero: ')
    try:
        entrada_int = int(entrada)
        if entrada_int % 2 == 0:
            print('Esse numero e par')
        else:
            print('Esse numero e impar')
            
        break
    except ValueError:
        os.system('cls')
        print('Por favor digite um numero')
        continue