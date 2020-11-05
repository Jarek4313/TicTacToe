import os

from player_class import Player
from game_mode_class import Game_Mode
from dificult_level_class import Dificult_Level
from draw_menu import draw_logo
class Game:
    def __init__(self):
        self.__player_one = None
        self.__player_two = None
        #self.__difficulty_level = None
        self.__difficulty_level = Dificult_Level()
        #self.__game_mode = None
        self.__game_mode = Game_Mode()

    # @property
    # def Game_Mode(self):
    #     return self.__game_mode
    # @Game_Mode.setter
    # def Game_Mode(self, new_game_mode):
    #     self.__game_mode = new_game_mode

    def Set_Game_Mode(self, game_mode):
        #self.__game_mode = Game_Mode()
        self.__game_mode = game_mode

    def Set_Difficulty_Level(self, difficulty_level):
        #self.__difficulty_level = Dificult_Level()
        self.__difficulty_level = difficulty_level

    def Set_Players_Name(self):
        self.__player_one = Player()
        self.__player_two = Player()

        os.system("cls || clear")
        
        if self.__game_mode.Mode == "player-player":
            draw_logo('set name player one')
            tmp_name = input("Podaj imię gracza pierwszego: ")
            self.__player_one.Name = tmp_name

            os.system("cls || clear")

            draw_logo('set name player two')
            tmp_name = input("Podaj imię gracza drugiego: ")
            self.__player_two.Name = tmp_name

        elif self.__game_mode.Mode == "player-computer":
            draw_logo('set name player')
            tmp_name = input("Podaj imię gracza: ")
            self.__player_one.Name = tmp_name

        else:
            pass

    def Start_Game(self):
        os.system("cls || clear")

        print(self.__game_mode.Mode)
        print(self.__difficulty_level.Level)
        print(self.__player_one.Name)
        print(self.__player_two.Name)
        input("OK")
