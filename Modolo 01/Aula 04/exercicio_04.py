import os

class ClassRoom:
    def __init__(self, sala):
        self.classroom = sala

    def check_student(self, student):
        return print(True if student in self.classroom else False)
    
salas = {
        '1A':["Maria Fernanda", "George", "Pablo", "Lucas", "Marco", "Tony", "Diego"],
        '2A':["Carlos", "Wilke", "Jhon", "Ana Beatriz", "Rafaela", "Eduarda", "Walter"],
        '3A':["Roberta", "Pedro", "Eminem", "Felipe", "Camile", "Lais", "Laura"] 
        }

while True:
    print(*salas, sep=' | ')
    escolher_sala = input('Escolha uma das salas: ').upper()
    if escolher_sala in salas:
        break
    else:
        os.system('cls')
        print('Digite uma sala valida')
        continue

while True:
    aluno = input('Digite o nome do aluno: ').title()
    if aluno.isspace() or aluno == '':
        continue
    else:
        break

room_one = ClassRoom(salas[escolher_sala])

room_one.check_student(aluno)