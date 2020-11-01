import os
import time
from user_input import input_from_user


#funkcja "czuwająca" nad tym, aby kursor w menu zawsze wskazywał na pozycję menu i nie dało się wyjść poza opcje
def set_arrow_idnication(arrow_idnication, arrow_options):
    if arrow_idnication < 0:
        return len(arrow_options)-1
    elif arrow_idnication > len(arrow_options)-1:
        return 0
    else:
        return arrow_idnication

def set_arrow_options(arrow_options, arrow_indication):
    
    for i in range(len(arrow_options)):
        if i == arrow_indication:
            arrow_options[i] = "<-"
        else:
            arrow_options[i] = " "
        i += 1
    return arrow_options

def result_draw_menu(menu_to_draw,tmp_arrow_indication):
    i = 0
    for index in dict(menu_to_draw).values():
        if i == tmp_arrow_indication:
            return index
        i += 1

def draw_menu(menu_to_draw):
    
    arrow_indication = 0
    arrow_options = [] 
    menu_options = [] 

    for name in dict(menu_to_draw).keys():
        arrow_options.append(" ")
        menu_options.append(name)

    while True:
        os.system("cls || clear")        
                
        arrow_options = set_arrow_options(arrow_options,arrow_indication)                

        for item,arrow in zip(menu_options,arrow_options):
            print(item + " "+ arrow)
        
        tmp_arrow_indication = arrow_indication

        arrow_indication += input_from_user()
                
        if arrow_indication >= 100:            
            arrow_indication = 0
            time.sleep(0.14)
            return result_draw_menu(menu_to_draw, tmp_arrow_indication)

        arrow_indication = set_arrow_idnication(arrow_indication, arrow_options)

        time.sleep(0.2)