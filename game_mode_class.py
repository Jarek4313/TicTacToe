class Game_Mode:
    def __init__(self):
        self.__mode = None
    
    @property
    def Mode(self):
        return self.__mode

    @Mode.setter
    def Mode(self, new_mode):
        if new_mode == 20:
            self.__mode = 'player-player'
        elif new_mode == 21:
            self.__mode = 'player-computer'
        elif new_mode == 22:
            self.__mode = 'computer-computer'
        else:
            print("Brak takiego trybu!")
            self.__mode = None

    @Mode.deleter
    def Mode(self):
        self.__mode = None

# gm = Game_Mode()
# gm.Mode = 20
# print(gm.Mode)