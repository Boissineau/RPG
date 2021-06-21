from board import Board
import random
import threading
import time
import string

class Entity:
    def __init__(self, board, rows, cols):
        # entity settings
        self.board = board
        self.x = random.randint(0, cols-1)
        self.y = random.randint(0, rows-1)
        self.rows = rows - 1
        self.cols = cols - 1
        self.name = ''.join(random.choice(string.ascii_letters) for i in range(10))

        # entity specifics
        self.hp = random.randint(50, 120)
        self.atk = random.randint(5, 20)
        self.action = False



        board.entity_list(self)
        self._loop()







    def _loop(self):
        while(1):
            if self.board.nearby(self.x, self.y, self.name):
                self.action = True
                continue
            if self.action:
                self._fighting()
            else:
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
        

    def _fighting(self):
        time.sleep(1)
        self.action = False
        self._move()

    def get_state(self):
        return self.action

    def get_name(self):
        return self.name

    def get_position(self):
        return self.x, self.y


