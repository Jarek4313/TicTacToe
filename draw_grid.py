
import math
import os
from user_input import game_play_input
import time

def draw_grid(pozycja):
    grid = ""
    for i in range(28):
        grid += "="
    grid += "\n"
    tmp = 1

    for i in range(9):
        for i in range(4):
            grid += "|"
            grid += "        "
        grid += "\n"

        if tmp % 3 == 0:
            for i in range(28):
                grid += "="
            grid += "\n"
        tmp += 1

    mod_x = 0
    mod_y = 0
    tmp_grid = ""
    
    for item in range(len(grid)):
        if pozycja <= 2:
            mod_x = pozycja
        
        if pozycja > 2:
            mod_x = pozycja - 3
            mod_y = 140

        if pozycja > 5:
            mod_x = pozycja - 6
            mod_y = 280

        if item >= mod_y + 69 + (mod_x*9)   and item <= mod_y + 72 + (mod_x*9) :
            tmp_grid += "_"
        else:
            tmp_grid += grid[item]

    
    return tmp_grid

def draw_grid_validation_position_input(position):
    if position >= 99:
        return position - 99

    if position < 0:
        return 0
    elif position > 8:
        return 8
    else:
        return position

def draw_grid_make_mark(condition, index, lista, znak):
    if condition >= 99:
        lista[index] = znak
        return lista
    else:
        pass