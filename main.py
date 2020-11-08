from draw_menu import draw_menu
from const_variables import main_menu
from const_variables import set_difficulty_level_menu
from const_variables import game_mode_menu
from const_variables import game_logo

from game_class import Game
from dificult_level_class import Dificult_Level
from player_class import Player
from game_mode_class import Game_Mode

def main():

    #główne obiekty projektu
    difficult_level = Dificult_Level()
    game_mode = Game_Mode()
    game = Game()

    is_game_is_process = True
    while is_game_is_process:

        menu_option = draw_menu(main_menu, game_logo)


        if menu_option == 0:
            menu_option = draw_menu(game_mode_menu, 'set game mode')

            if not menu_option == 3:
                game_mode.Mode = menu_option                
                
                game.Set_Game_Mode(game_mode)
                game.Set_Difficulty_Level(difficult_level)     
                game.Set_Players_Name()
                game.Set_Cpu()
                game.Start_Game()
                #game.End_Game()
                        
            menu_option = None

        if menu_option == 2:
            menu_option = draw_menu(set_difficulty_level_menu, 'difficulty level')
            difficult_level.Level = menu_option
            menu_option = None

        if menu_option == 3:
            input("Exit")
            is_game_is_process = False

if __name__ == "__main__":
    main()
