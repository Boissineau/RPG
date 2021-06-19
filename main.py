from grid import Grid
from entity import Entity

import threading
import time



def move_entities(entity, board):
    x, y = entity.get_location()
    board.remove(x, y)
    x, y = entity.update_location()
    board.move(x, y)
    return entity, board








if __name__ == '__main__':
    row = 20
    col = 20
    board = Grid(row, col)
    entities = []
    for i in range(5):
        entity = Entity(row, col)
        entities.append(entity)

    while(1):  
        time.sleep(2) 
        for idx, i in enumerate(entities):
            entities[idx], board = move_entities(i, board)
        for i in board.get_grid():
            print(i)
    
    