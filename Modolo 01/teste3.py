class Robots():    
    robot_default = """
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
            // \\ / |O|======|O| \  //\\
            |  |  | |O+------+O| |  |  |
            |\/|  \_+/        \+_/  |\/|
            \__/  _|||        |||_  \__/
                  | ||        || |      
                 [==|]        [|==]     
                 [===]        [===]     
                  >_<          >_<      
                 || ||        || ||     
                 || ||        || ||     
                 || ||        || ||     
               __|\_/|__    __|\_/|__   
              /___n_n___\  /___n_n___\  
    """

    robot_attributes = r"""
        -------------------------
        0: {head_name}|1: {weapon_name}
        Is available: {head_status}|Is available: {weapon_status}
        Attack: {head_attack}|Attack: {weapon_attack}
        Defense: {head_defense}|Defense: {weapon_defense}
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
lista_1 = ['papel', 'tesoura', 'lapis']
lista_2 = []
for i, item in enumerate(lista_1):
    lista_2.append(item + item)

print(lista_2)