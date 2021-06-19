import random
import threading
import time
from grid import Grid
class Entity:
    def __init__(self, row, col):
        self.row = row - 1
        self.col = col - 1
        self.x = random.randint(0, col-1)
        self.y = random.randint(0, row-1)
        self.hp = random.randint(50, 150)
        self.atk = random.randint(1, 20)
        # thread = threading.Thread()
        # thread.start()



    def update_location(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        if self.x < 0:
            self.x = 0
        if self.x > self.col:
            self.x = self.col
        if self.y < 0:
            self.y = 0
        if self.y > self.row:
            self.y = self.row
        return self.x, self.y
            

    def get_location(self):
        return self.x, self.y
    def get_stats(self):
        return self.hp, self.atk
    def get_hp(self):
        return self.hp

