import random

class Computer:
    def __init__(self):
        self.__name = 'CPU'

    @property    
    def Random(self):
        return random.randint(0,8)


