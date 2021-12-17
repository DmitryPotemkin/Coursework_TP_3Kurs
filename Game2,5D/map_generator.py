from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32
import random

_ = False
    # Генерация карты
def map_gen(a, b):
    width = a
    height = b
    drunk = {
        'wallCountdown': 100,
        'padding': 1,
        'x': int(width / 2),
        'y': int(height / 2)
    }

    level = [([1] * width) for _ in range(height)]

    while drunk['wallCountdown'] >= 0:
        x = drunk['x']
        y = drunk['y']
        if level[y][x] == 1:
            level[y][x] = False
            drunk['wallCountdown'] -= 1
        roll = random.randint(1, 4)
        if roll == 1 and x > drunk['padding']:
            drunk['x'] -= 1
        if roll == 2 and x < width - 1 - drunk['padding']:
            drunk['x'] += 1
        if roll == 3 and y > drunk['padding']:
            drunk['y'] -= 1
        if roll == 4 and y < height - 1 - drunk['padding']:
            drunk['y'] += 1

    for i in range(1,height):
        for j in range(1,width // 2):
            if i == 1 and level[i][j] != False:
                level[i][j] = False
            elif j == width // 2 - 1 and level[i][j] != False:
                level[i][j] = False
            elif j == width // 2 - 1 and level[i][j] == False or i == 1 and level[i][j] == False:
                return level

    # Заполнение данных карты
def mapCreate(lvl):
    if lvl == 1:
        matrix_map = [
            [1,1,1,1,2,1,1,1,1,1,1,1],
            [1,_,_,_,_,_,_,_,2,_,_,1],
            [1,_,_,_,_,_,_,_,2,_,_,1],
            [1,_,_,_,_,_,_,_,2,_,_,1],
            [1,1,1,_,_,_,_,_,2,_,_,1],
            [1,_,_,_,_,_,_,_,_,_,_,2],
            [1,_,_,_,_,_,_,_,_,_,_,1],
            [1,1,1,1,1,1,1,2,1,1,1,1]
            ]
    elif lvl == 2:
        matrix_map = [
            [1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
            [1,_,_,_,_,_,_,_,_,2,1,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,1,_,_,_,_,_,_,_,1,1,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,2,1,1],
            [1,2,1,_,_,_,_,_,1,_,_,2,_,_,_,_,_,1,_,_,_,2,1,1],
            [1,1,2,_,_,_,_,_,_,_,_,2,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,_,_,_,_,_,_,_,_,_,_,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,_,1,1,1,1,1,2,1,1,1,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,_,1,1,2,1,1,1,1,1,1,1,1,1,1,_,2,_,1,_,1,1,1,1],
            [1,_,_,_,_,_,_,_,_,2,1,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,1,_,_,_,_,_,_,_,1,1,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,_,_,_,_,_,_,_,1,_,_,1,_,_,_,_,_,_,_,_,_,2,1,1],
            [1,2,1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,2,_,_,_,2,1,1],
            [1,1,2,_,_,_,_,_,_,_,_,2,1,_,_,_,_,2,2,2,_,2,1,1],
            [1,_,_,_,_,_,_,_,_,_,_,1,1,_,_,_,_,_,_,_,_,2,1,1],
            [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1]
            ]
    elif lvl == 3:
        matrix_map = [
            [1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
            [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
            [1,1,1,1,1,1,1,1,1,_,_,_,_,_,_,1,1,1,1,1,1,1,1,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,1,_,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,1,1,1,1,1,1,1,1,1,1,_,_,1,1,1,1,1,1,1,_,1,1,1],
            [1,_,_,_,_,_,_,_,_,_,1,_,_,1,_,_,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,_,_,1,_,_,1,_,_,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,_,_,_,_,_,1,_,_,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
            [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1]
            ]
    else:
        matrix_map = map_gen(24, 16)
    world_width = len(matrix_map[0]) * tile
    world_height = len(matrix_map) * tile
    world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
    mini_map = set()
    collision_walls = []
    for j, row in enumerate(matrix_map):
        for i, char in enumerate(row):
            if char:
                mini_map.add((i * map_tile, j * map_tile))
                collision_walls.append(pygame.Rect(i * tile, j * tile, tile, tile))
                if char == 1:
                    world_map[(i * tile, j * tile)] = 1
                elif char == 2:
                    world_map[(i * tile, j * tile)] = 2
    return matrix_map, world_width, world_height, world_map, mini_map, collision_walls


matrix_map, world_width, world_height, world_map, mini_map, collision_walls = mapCreate(1)
