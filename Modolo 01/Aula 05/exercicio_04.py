import os

validar_senha = '123'
verification_code = '9898'

tentativas = 0

for n in range(3):
    senha_input = input('Digite sua senha: ')
    code_input = input('Digite o codigo de verificacao: ')
    if senha_input == validar_senha and code_input == verification_code:
        break
    else:
        tentativas += 1
        os.system('cls')
        continue

if tentativas == 3:
    print('Sua conta foi bloqueada')
else:
    print('Sua conta foi verificada')