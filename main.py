import time
from board import Board 
from entity import Entity
import threading
import numpy as np
entities = []

def loop(board):
    while(1):
        time.sleep(1)
        print(np.array(board.grid))
        for i in board.get_entities():
            if i.get_state():
                print(f'{i.get_name()} is fighting!')
        # print('\033[F'*23)
        print()

def create_entity(board, rows, cols):
    Entity(board, rows, cols)


if __name__ == '__main__':

    rows = 20
    cols = 20
    board = Board(rows, cols)
    for i in range(5):
        thread = threading.Thread(target=create_entity, args=(board, rows, cols))
        thread.start()



    loop(board)
