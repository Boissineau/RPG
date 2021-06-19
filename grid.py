import random
class Grid:

    def __init__(self, row=1, col=1):

        self.grid = [[0]*col for i in range(row)]
        self.entities = 0

    def get_grid(self):
        return self.grid


    def move(self, x, y):
        self.grid[y][x] = 1


    def remove(self, x, y):
        self.grid[y][x] = 0
