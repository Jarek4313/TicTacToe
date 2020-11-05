class Dificult_Level:
    def __init__(self, level):
        self.__level = level

    @property
    def Level(self):
        return self.__level
    @Level.setter
    def Level(self, newLevel):
        if newLevel == 10:
            self.__level = "easy"
        if newLevel == 11:
            self.__level = 'normal'
        elif newLevel == 12:
            self.__level = 'limbo'
        else:
            self.__level = None
        
    @Level.deleter
    def Level(self):
        self.__level = None
