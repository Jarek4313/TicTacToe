import sys
from const_variables import alpha_numeric_upper_and_down

#sys.path.append('c:/TicTacToe/function_folder/')
#from ...app.function_folder.const_variables import alpha_numeric_upper_and_down
#functoconst_variables import alpha_numeric_upper_and_down

class Player:
    def __init__(self, mark):
        self.__name = None
        self.__poziom = None
        self.__mark = mark
        self.__win = False

    @property
    def Win(self):
        return self.__win
    @Win.setter
    def Win(self, win):
        self.__win = win
        
    @property 
    def Mark(self):
        return self.__mark

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
