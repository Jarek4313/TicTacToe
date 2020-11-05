from draw_menu import draw_menu
from const_variables import main_menu
from const_variables import set_dificult_level_menu
from const_variables import game_mode_menu
from dificult_level_class import Dificult_Level
from player_class import Player

def main():
    #print("-"*80,"main OK")

    #główne obiekty projektu
    dificult_level = Dificult_Level(11)
    player_one = Player()
    player_two = Player()
    game_mode = 
    while True:

        menu_option = draw_menu(main_menu,'tictactoe')


        if menu_option == 0:
            menu_option = draw_menu(game_mode_menu, 'abc')
            # while player_one.Name == None:
            #     name = input("Podaj imię: ")
            #     player_one.Name = name
            
            menu_option = None

        if menu_option == 2:
            menu_option = draw_menu(set_dificult_level_menu, 'difficultylevel')
            dificult_level.Level = menu_option
            menu_option = None

        if menu_option == 3:
            input("Exit")
            return




if __name__ == "__main__":
    main()
