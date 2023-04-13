import os

class DesempenhoAcademico():

  def __init__(self, aluno):
    self.nomeAluno = aluno
    self.media = 0
    self.situacao = 0
    os.system('cls')
    print(aluno)

  def calcularMedia(self, nota1, nota2, *_):
    self.media = (nota1 + nota2) / 2
    if self.media >= 7.00:
      self.situacao = 1
    print(f'Notas: {float(nota1)} e {float(nota2)}')
    print(f'Media: {self.media}')
    print()
    return self.media

  def calcularMediaAposFinal(self, notaFinal):
    self.media = (self.media + notaFinal) / 2
    if self.media >= 5:
      self.situacao = 2
    print(f'Nota da Final: {float(notaFinal)}')
    print(f'Media apos Final: {self.media}')
    return self.media

  def situacaoAluno(self):
    if self.situacao == 1 and self.media >= 7:
      print(f'Aluno "{self.nomeAluno}" foi Aprovado')
    elif self.situacao == 2 and self.media >= 5:
      print(f'Aluno "{self.nomeAluno}" foi Aprovado na Final')
    else:
      print(f'Aluno "{self.nomeAluno}" foi Reprovado')


sala1 = {'Julia': [2, 8, 3], 'Vitor': [10, 10], 'Jonathan': [7, 6, 5], \
         'Jhonny': [2, 0, 10], 'Ana': [9, 8], 'Megan': [7, 7]}

print('Alunos do 1°C: ')
print(*sala1, sep=' | ')

estudante = ''
while estudante not in sala1:
  estudante = input('Qual o nome do estudante? ')

desempenho = DesempenhoAcademico(estudante)
primeira_media = desempenho.calcularMedia(*sala1[estudante])
final_media = 0

if primeira_media < 7:
  final_media = desempenho.calcularMediaAposFinal(sala1[estudante][2])

desempenho.situacaoAluno()
