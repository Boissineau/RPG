from board import Board
import random
import threading
import time


class Entity:
    def __init__(self, board, rows, cols):
        self.board = board
        self.x = random.randint(0, cols-1)
        self.y = random.randint(0, rows-1)
        self.rows = rows - 1
        self.cols = cols - 1
        self._loop()
        board.entity_list(self)
    def _loop(self):
        while(1):
            time.sleep(1)
            self._move()
        

    def _move(self):
        x = self.x
        y = self.y 
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        if self.x < 0:
            self.x = 0
        if self.x > self.cols:
            self.x = self.cols
        if self.y < 0:
            self.y = 0
        if self.y > self.rows:
            self.y = self.rows
        self.board.update_board(x, y, self.x, self.y)
        



