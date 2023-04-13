import os

class Aluno:
  def __init__(self, nome_completo, idade, serie, turno, pai, mae, contato, alergia):
    self.nome_completo = nome_completo
    self.idade = idade
    self.serie = serie
    self.turno = turno
    self.pai = pai
    self.mae = mae
    self.contato = contato
    self.alergia = alergia

  def imprimirFichaAluno(self):

    print(f'Nome do Aluno: {self.nome_completo}',\
          f'Idade: {self.idade}',       \
          f'Serie: {self.serie}',       \
          f'Turno: {self.turno}',       \
          f'Pai: {self.pai}',           \
          f'Mae: {self.mae}',           \
          f'Contato: {self.contato}', sep='\n'
          )
    if self.alergia == True:
        print(f'Alergico [S] ou [N]: {alergia_aluno}')
        self.doenca = input('Digite qual a alergia do aluno: ')


       
      
    
nome_aluno = input('Digite o nome completo do Aluno: ')
idade_aluno = input('Digite a idade: ')
serie_aluno = input('Digite a serie: ')
turno_aluno = input('Digite o turno: ')
pai_aluno = input('Digite o nome completo do pai: ')
mae_aluno = input('Digite o nome completo da mae: ')
contato_aluno = input('Digite o numero para contato: ')
alergia_aluno = input('Alergico [S] ou [N]: ')

alergia_bool = False
if alergia_aluno == 'S':
   alergia_bool = True

lista_aluno = [nome_aluno, idade_aluno, serie_aluno, turno_aluno, \
                pai_aluno, mae_aluno, contato_aluno, alergia_bool]

os.system('cls')
print()

aluno1 = Aluno(*lista_aluno)
aluno1.imprimirFichaAluno()