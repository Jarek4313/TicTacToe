import os
import time
from user_input import input_from_user
from const_variables import alpha_ascii_list

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

def draw_menu(menu_to_draw, logo=""):
    
    #zmienne pomocnicze
    arrow_indication = 0 #aktualna pozycja kursora 
    arrow_options = []  #sloty dla kursora, odpowiadają ilości opcji w menu
    menu_options = []  #właściwe opcje w menu

    #uzupełnienie list z przesłanego zestawu menu
    for name in dict(menu_to_draw).keys():
        arrow_options.append(" ")
        menu_options.append(name)


    #właściwa pętla rysowania menu
    while True:
        os.system("cls || clear")        
        
        #rysowanie logo
        if not logo == "":
            draw_logo(logo)

        #do listy arrow_options na indeksie arrow_indication wstawia kursor "<-"
        arrow_options = set_arrow_options(arrow_options,arrow_indication)                

        #rysowanie kolejnych opcji z menu oraz kursoru 
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

def draw_logo(logo):
    path = r'c:\TicTacToe\ascii_alphabet.txt'
    ascii_logo_to_draw = []

    try:
        with open(path, 'r', encoding="UTF-8") as file:
            content = file.readlines()    
    except FileExistsError:
        print("Plik nie istnieje")

    for i in range(len(content)):
        content[i] = content[i].strip()
      
    for char_in_logo in logo:
        tmp = 0
        for char in alpha_ascii_list:
            if char == char_in_logo:
                break            
            tmp += 1        
       
        i = 0
        if ascii_logo_to_draw == []:
            for i in range(7):
                ascii_logo_to_draw.append(content[i + (tmp * 7)])
                i += 1
        else:
            for i in range(7):
                ascii_logo_to_draw[i] += content[i + (tmp * 7)]
                i += 1

    for item in ascii_logo_to_draw:
        #print(str(i)+":"+str(i+1) + item)
        print(item)



