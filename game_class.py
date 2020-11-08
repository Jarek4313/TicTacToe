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
        self.__actual_player = None

    def Set_Game_Mode(self, game_mode):
        self.__game_mode = game_mode

    def Set_Difficulty_Level(self, difficulty_level):
        self.__difficulty_level = difficulty_level

######################################################################################
# Pobranie i walidacja właściwości Name dla __player_one i __player_two
    def Set_Players_Name(self):
        self.__player_one = Player('X')
        self.__player_two = Player('O')
        
        if self.__game_mode.Mode == "player-player":
            while self.__player_one.Name == None:
                os.system("cls || clear")
                draw_logo('name player one')
                tmp_name = input("Podaj imię gracza pierwszego: ")
                self.__player_one.Name = tmp_name
                
            while self.__player_two.Name == None:
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
######################################################################################
# Wyświetlanie informacji o rozgrywce
    def draw_game_info(self):
        #print(self.__game_mode.Mode)
        if self.__game_mode.Mode == 'player-player':
            print("Aktualany gracz {} znak {}".format(self.__actual_player.Name, self.__actual_player.Mark))
            print("Aktualne punkty: {:.2f}".format(self.__actual_player.Time))
            
        # if self.__game_mode.Mode == 'player-computer':
        #     print("Gracz: {}".format(self.__player_one.Name))
        #     print("Gracz:")
#####################################
######################################################################################
# Przełączenie graczy w zależności czy wykonał ruch, gracz musi postawić swój znak w wolnym miejscu na siatce
    def switch_round(self,game_input,input_makr_in_free_slot):
        if game_input >= 99 and input_makr_in_free_slot:            
            print('switch')
            if self.__actual_player == self.__player_one:
                self.__actual_player = self.__player_two
                #return self.__player_two.Mark
            else:
                self.__actual_player = self.__player_one
                #return self.__player_one.Mark
        # else:
        #     return actual_mark
######################################################################################
# Sprawdzanie czy wystąpił warunek zwycięstwa
    def check_win_condition_for_gamer(self, grid_list, mark):
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
        if self.check_win_condition_for_gamer(grid_list, self.__player_one.Mark):
            #self.__player_one.Win = True
            self.__actual_player = self.__player_one
            self.__actual_player.Win = True
            return False

        if self.check_win_condition_for_gamer(grid_list, self.__player_two.Mark):
            #self.__player_two.Win = True
            self.__actual_player = self.__player_two
            self.__actual_player.Win = True
            return False

        return True
#####################################
######################################################################################
# Sprawdzanie czy wystąpił warunek zwycięstwa
    def Start_Time(self):
        return self.__actual_player.Counter_Time(True, 0)
    def Stop_Time(self, __time):
        self.__actual_player.Counter_Time(False,__time)

    def Start_Game(self):
        os.system("cls || clear")
        game_input_value = 0
        game_input_value_only_grid_position = 0
        grid_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        continue_game_condition = True
        input_mark_in_free_slot = True
        self.__actual_player = self.__player_one
        
        while continue_game_condition:
            os.system("cls || clear")

            print(draw_grid(game_input_value, grid_list))
            
            self.draw_game_info()
            
            continue_game_condition = self.check_win_condition(grid_list)
            if not continue_game_condition:
                break
            
            __time = self.Start_Time()
            
            game_input_value += game_play_input()
            if game_input_value >= 99:
                input_mark_in_free_slot = draw_grid_make_mark(game_input_value_only_grid_position, grid_list, self.__actual_player.Mark)
            
            self.switch_round(game_input_value, input_mark_in_free_slot)
            
            self.Stop_Time(__time)

            game_input_value = draw_grid_validation_position_input(game_input_value)
            game_input_value_only_grid_position = game_input_value

            time.sleep(0.21)

    def End_Game(self):
        os.system("cls || clear")
        draw_logo("you win !")
        print("Brawo wygrałeś: {}".format(self.__actual_player.Name))
        print("Twój wynik: {:.2f}".format(self.__actual_player.Time))
        input()