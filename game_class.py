import os
import time

from draw_grid import draw_grid
from draw_grid import draw_grid_validation_position_input
from draw_grid import draw_grid_make_mark
from user_input import game_play_input

from player_class import Player
from game_mode_class import Game_Mode
from dificult_level_class import Dificult_Level
from computer_class import Computer

from draw_menu import draw_logo
class Game:
    def __init__(self):
        self.__player_one = None
        self.__player_two = None
        self.__cpu = None
        self.__difficulty_level = Dificult_Level()
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
        self.__player_one = Player('X')
        self.__player_two = Player('O')

        os.system("cls || clear")
        
        if self.__game_mode.Mode == "player-player":
            draw_logo('name player one')
            tmp_name = input("Podaj imię gracza pierwszego: ")
            self.__player_one.Name = tmp_name

            os.system("cls || clear")

            draw_logo('name player two')
            tmp_name = input("Podaj imię gracza drugiego: ")
            self.__player_two.Name = tmp_name

        elif self.__game_mode.Mode == "player-computer":
            draw_logo('set name player')
            tmp_name = input("Podaj imię gracza: ")
            self.__player_one.Name = tmp_name
        else:
            pass

    def Set_Cpu(self):
        if self.__game_mode.Mode == "player-computer":
            self.__cpu = Computer()

    def draw_game_info(self):
        print(self.__game_mode.Mode)
        if self.__game_mode.Mode == 'player-computer':
            print("Gracz: {}".format(self.__player_one.Name))
            print("Gracz:")

    def switch_round(self, actual_mark, game_input):
        if game_input >= 99:            
            print('switch')
            if actual_mark == self.__player_one.Mark:
                return self.__player_two.Mark
            else:
                return self.__player_one.Mark
        else:
            return actual_mark

    def check_win_condition_for_part(self, grid_list, mark):
        row_point = [0,0,0]
        column_point = [0,0,0]
        diagonal_point = [0,0]
        for i in range(3):
            if grid_list[i] == mark:
                row_point[0] += 1
            if grid_list[3+i] == mark:
                row_point[1] += 1
            if grid_list[6+i] == mark:
                row_point[2] += 1
            
            if grid_list[i*3] == mark:
                column_point[0] += 1
            if grid_list[1+(i*3)] == mark:
                column_point[1] += 1
            if grid_list[2+(i*3)] == mark:
                column_point[2] += 1

            if grid_list[i*4] == mark:
                diagonal_point[0] += 1
            if grid_list[2 + i*2] == mark:
                diagonal_point[1] += 1
             
        if max(row_point) == 3:
            return True
        if max(column_point) == 3:
            return True
        if max(diagonal_point) == 3:
            return True
    def check_win_condition(self, grid_list):
        if self.check_win_condition_for_part(grid_list, self.__player_one.Mark):
            self.__player_one.Win = True
            return True
        if self.check_win_condition_for_part(grid_list, self.__player_two.Mark):
            self.__player_two.Win = True
            return True
        return False

    def Start_Game(self):
        os.system("cls || clear")
        game_input = 0
        game_position_index = 0
        grid_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        actual_mark = self.__player_one.Mark

        while True:
            os.system("cls || clear")
            print(draw_grid(game_input, grid_list))
            self.draw_game_info()
            print(actual_mark)

            game_input += game_play_input()
            draw_grid_make_mark(game_input, game_position_index, grid_list, actual_mark)
            
            actual_mark = self.switch_round(actual_mark, game_input)
            

            if self.check_win_condition(grid_list):
                input("Wygrana!")
                break

            game_input = draw_grid_validation_position_input(game_input)
            game_position_index = game_input

            

            time.sleep(0.21)
            
            
        #print(self.__game_mode.Mode)
        #print(self.__difficulty_level.Level)
        #print(self.__player_one.Name)
        #print(self.__player_two.Name)
        #input("OK")
