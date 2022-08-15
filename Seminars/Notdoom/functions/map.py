from settings import *

text_map = [
    '113111311131',
    '1.....2....1',
    '1.22.....2.1',
    '3..........1',
    '1.22.......3',
    '1.2......2.1',
    '3.....2....1',
    '111131111311'
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
            elif char == '3':
                world_map[(i * TILE, j * TILE)] = '3'