import sys
from const_variables import alpha_numeric_upper_and_down

#sys.path.append('c:/TicTacToe/function_folder/')
#from ...app.function_folder.const_variables import alpha_numeric_upper_and_down
#functoconst_variables import alpha_numeric_upper_and_down

class Player:
    def __init__(self):
        self.__name = None
        self.__poziom = None

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, new_name):
        incorect_char = False
        if len(new_name) <= 20:
            for item in new_name:
                if not item in alpha_numeric_upper_and_down:
                    incorect_char = True
                    break
            if not incorect_char:
                self.__name = new_name
            else:
                print("Niewłaściwy znak!")
        else:
            print("Liczba znaków przekracza 20")

    @Name.deleter
    def Name(self):
        self.__name = None
