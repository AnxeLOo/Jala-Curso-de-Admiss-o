import os
import math
import time

colors = {
        "Black": '\x1b[90m',
        "Blue": '\x1b[94m',
        "Cyan": '\x1b[96m',
        "Green": '\x1b[92m',
        "Magenta": '\x1b[95m',
        "Red": '\x1b[91m',
        "White": '\x1b[97m',
        "Yellow":'\x1b[93m',
    }

def centerText(text, space):
    text = str(text).strip()
    leftChars = space - len(text)
    leftChars = leftChars + 1 if leftChars % 2 == 1 else leftChars
    return (int(leftChars/2) * ' ') + text

def addSpaces(text, spaces, left = 0, forceCenter = True):
    text = (left * ' ') + str(text).rstrip()
    if forceCenter == True:
        text = centerText((left * ' ') + str(text).rstrip(), spaces)
    return text + (int(spaces - len(text)) * ' ')

class Part():
    
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption = 0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = math.ceil(attack_level * 1.5) if energy_consumption == 0 else energy_consumption
        
    def get_status_dict(self, suffix=""):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name{}".format(formatted_name, suffix): addSpaces(self.name.upper(), 22, forceCenter = False),
            "{}_status{}".format(formatted_name, suffix): addSpaces(self.is_available(), 11, forceCenter = False),
            "{}_attack{}".format(formatted_name, suffix): addSpaces(self.attack_level, 17, forceCenter = False),
            "{}_defense{}".format(formatted_name, suffix): addSpaces(self.defense_level, 16, forceCenter = False),
            "{}_energy_consump{}".format(formatted_name, suffix): addSpaces(self.energy_consumption, 5, forceCenter = False)
        }
    
    def reduce_edefense(self, attack_level):
        self.defense_level = self.defense_level - attack_level
        if self.defense_level <= 0:
            self.defense_level = 0
    
    def is_available(self):
        return self.defense_level > 0
    
class Robots():
    def __init__(self, name, color_code, robot_design):
        self.name = name
        self.color_code = color_code
        self.robot_design = robot_design
        self.energy = 100
        self.last_round_weapon_was_used = 0
        self.parts = [
            Part("Head", attack_level=5, defense_level=10),
            Part("Weapon", attack_level=20, defense_level=0, energy_consumption=15),
            Part("Left Arm", attack_level=3, defense_level=20),
            Part("Right Arm", attack_level=6, defense_level=20),
            Part("Left Leg", attack_level=4, defense_level=20),
            Part("Right Leg", attack_level=8, defense_level=20),
        ]
        self.robot_list = []
        self.robot_interface = []

    robot_default = {
'1' : r"""
     ____          ____
    |oooo|  ____  |oooo|
    |oooo| '    ' |oooo|
    |oooo|/\_||_/\|oooo|
    '----´ / __ \ `----'
   '/  |#|/\/__\/\|#|  \'
   /  \|#|| |/\| ||#|/  \
  / \_/|_|| |/\| ||_|\_/ \
 |_\/    O\=----=/O    \/_|
 <_>      |=\__/=|      <_>
 <_>      |------|      <_>
 | |   ___|======|___   | |
 //\\ / |O|======|O| \  //\\
 |  | | |O+------+O| |  |  |
 |\/| \_+/        \+_/  |\/|
 \__/ _|||        |||_  \__/
      | ||        || |
     [==|]        [|==]
     [===]        [===]
      >_<          >_<
     || ||        || ||
     || ||        || ||
     || ||        || ||
   __|\_/|__    __|\_/|__
  /___n_n___\  /___n_n___\
""", 
'2' : r"""
     ____          ____ 
    |oooo| |\__/| |oooo|
    |oooo| 0_  _0 |oooo|
    |oooo|/\_||_/\|oooo|
 ___'----´ /_||_\ `----'___
 \ '/  |0|\_/__\_/|0|  \' /
  \   \|0|| |/\| ||0|/   /
  //\_/|_|| \__/ ||_|\_/\\
 |_//    [\=-\/-=/]    \\_|
 <_>      |=\__/=|      <_>
 <_>      |--||--|      <_>
 | |   ___|==||==|___   | |
 //\\ / |Y|==||==|Y| \  //\\
 |--| | |O+------+O| |  |--|
 |\/| \_+/        \+_/  |\/|
 \/\/ _|||        |||_  \/\/
      | ||        || |
     /==||        ||==\
     \===/        \===/
      >-<          >-<
     || ||        || ||
     || ||        || ||
     || ||        || ||
   __|\_/|__    __|\_/|__
  /___n_n___\  /___n_n___\
"""}

    robot_attributes = r"""
------------------------------------------------------------
0: {head_name}|1: {weapon_name}
Is available: {head_status}|Is available: {weapon_status}
Attack: {head_attack}|Attack: {weapon_attack}
Defense: {head_defense}|Defense: ∞               
Energy consumption: {head_energy_consump}|Energy consumption: {weapon_energy_consump}

2: {left_arm_name}|3: {right_arm_name}
Is available: {left_arm_status}|Is available: {right_arm_status}
Attack: {left_arm_attack}|Attack: {right_arm_attack}
Defense: {left_arm_defense}|Defense: {right_arm_defense}
Energy consumption: {left_arm_energy_consump}|Energy consumption: {right_arm_energy_consump}

4: {left_leg_name}|5: {right_leg_name}
Is available: {left_leg_status}|Is available: {right_leg_status}
Attack: {left_leg_attack}|Attack: {right_leg_attack}
Defense: {left_leg_defense}|Defense: {right_leg_defense}
Energy consumption: {left_leg_energy_consump}|Energy consumption: {right_leg_energy_consump}
"""
    
    def get_robot_attributes(self):
        formatted_attribute = [];
        attributes = self.robot_attributes.format(**self.get_part_status()).split('\n')
        for index, item in enumerate(attributes):
            formatted_attribute.append(addSpaces(item, 60, 5 if index > 1 else 0, False))
        return '\n'.join(formatted_attribute)

    def get_robot(self, index):
        formatted_robot = [];
        robot = self.robot_default[index].split('\n')
        for item in robot:
            formatted_robot.append(addSpaces(item, 60, 10))
        return '\n'.join(formatted_robot)
    
    def print_energy(self):
        return addSpaces(f'We have {self.energy}% percent energy left', 60, forceCenter=True) + '\n'
    
    def print_status(self):
        print(self.color_code)
        print('Hello my name is ', self.name)
        self.print_energy()
        robot = self.get_robot(self.robot_design) + self.get_robot_attributes()
        print(robot)
        print(colors['White'])
        print(52 * '-')

    def get_part_status(self, suffix=''):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict(suffix)
            part_status.update(status_dict)
        return part_status
    
    def battle_interface(self, robot2):
        self.robot_list = []
        
        # Define os robos centralizados
        robot_1 = (self.print_energy() + self.get_robot(self.robot_design)).split('\n')
        robot_2 = (robot2.print_energy() + robot2.get_robot(robot2.robot_design)).split('\n')

        for index, item in enumerate(robot_2):
            self.robot_list.append(self.color_code + robot_1[index] + colors["White"] + '|'
                                   + robot2.color_code + item)

        # Define e formata os STATUS dos robos
        robot_1 = self.get_robot_attributes()
        str_robot_1 = self.get_robot_attributes().split('\n')

        str_robot_2 = robot2.get_robot_attributes().split('\n')

        for index, item in enumerate(str_robot_2):
            self.robot_list.append(self.color_code + str_robot_1[index] + colors["White"] + '|'
                                   + robot2.color_code + item)
        
        print(*self.robot_list, sep= '\n')

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].reduce_edefense(self.parts[part_to_use].attack_level) 
        self.energy -= self.parts[part_to_use].energy_consumption
        if part_to_use == 1:
            self.disableWeapon()

    def enableWeapon(self, round):
        if (round - self.last_round_weapon_was_used) >= 5:
            self.parts[1].defense_level = 1

    def disableWeapon(self):
        self.parts[1].defense_level = 0

    def is_on(self):
        return self.energy >= 0
    
    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

def choose_robot():
    for index in range(len(Robots.robot_default)):
        print(f'{index + 1}): \n')
        print(Robots.get_robot(Robots, str(index + 1)))
    while True:
        chosen_robot = input('Choose a robot: ')
        if chosen_robot.isdigit() and chosen_robot in Robots.robot_default:
            break
    return chosen_robot

def build_robot():
    robot_selected = choose_robot()
    robot_name = input("Robot name: ")
    color_code = choose_color()
    robot = Robots(robot_name, color_code, robot_selected)
    robot.print_status()
    input('Press Enter to continue ')
    cls()
    return robot

def choose_color():
    print("Available colors:\n")
    for key, value in enumerate(list(colors)):
        print(colors["White"], key + 1, ')', colors.get(value), value)
    print(colors["White"])

    while True:
        chosen_color = input("Choose a color: ")
        if chosen_color.title() in colors:
            chosen_color = chosen_color.title()
            break
        elif chosen_color.isdigit():
            chosen_color = int(chosen_color)
            if chosen_color <= len(colors):
                chosen_color = list(colors)[chosen_color - 1]
                break
    return colors[chosen_color]

def cls():
    time.sleep(0.1)
    os.system('cls' if os.name=='nt' else 'clear')
    time.sleep(0.1)

def play():
    print('\033[0;0m')
    playing = True
    print("Welcome to the game!")
    print("Datas for player 1:")
    robot_one = build_robot()
    print("Datas for player 2:")
    robot_two = build_robot()
    
    current_robot = robot_one
    enemy_robot = robot_two
    round = 1

    while playing:
        sub_round = 0
        while sub_round < 2:
            cls()
            robot_one.battle_interface(robot_two)
            print(colors["White"])
            if sub_round == 0:
                current_robot = robot_one
                enemy_robot = robot_two
            else:
                current_robot = robot_two
                enemy_robot = robot_one
            part_to_use = 0

            while True:
                print(f'Round: {round}\nHey {current_robot.color_code}{current_robot.name}')
                attackParts = input(f"{colors['White']}What part should be used to attack and be attacked? (inform it like to_attack:to_be_attacked)\n")
                try:
                    part_to_use = attackParts.split(':')[0]
                    part_to_attack = attackParts.split(':')[1]
                except IndexError:
                    continue
                if part_to_use.isdigit() and part_to_attack.isdigit():
                    part_to_use = int(part_to_use)
                    part_to_attack = int(part_to_attack)
                    if part_to_use in range(6) and part_to_attack in range(6):
                        if current_robot.parts[part_to_use].is_available():
                            if part_to_attack != 1:
                                if part_to_use == 1:
                                    current_robot.last_round_weapon_was_used = round
                                break
            
            current_robot.attack(enemy_robot, part_to_use, part_to_attack)
            sub_round += 1

            robot_one.enableWeapon(round)
            robot_two.enableWeapon(round)
            print('\033[1;30;47m' + addSpaces('', 121))
            print(addSpaces(f"Round {round}", 121))
            print(addSpaces(f'{current_robot.name} caused {current_robot.parts[part_to_use].attack_level} damage to {enemy_robot.name} {enemy_robot.parts[part_to_attack].name}', 121))
            print(addSpaces('', 121) + '\033[0;0m')
            input("Press enter to continue")
            print()

            if current_robot.energy < current_robot.parts[part_to_use].energy_consumption or current_robot.energy < 5:
                playing = False
                print(f"Congratulations, {enemy_robot.color_code}{enemy_robot.name}{colors['White']} Won!!!!!!")
                print(f"Because, {current_robot.color_code}{current_robot.name} {colors['White']} run out of energy")
                break
        round += 1

        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print(f"Congratulations, {current_robot.color_code}{current_robot.name}{colors['White']} Won!!!!!!")
play()