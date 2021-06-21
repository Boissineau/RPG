
class Board:

    def __init__(self, rows, cols):
        self.rows = rows - 1
        self.cols = cols - 1
        self.grid = [[0]*cols for i in range(rows)]
        self.number_of_entities = 0
        self.entities = []


    def update_board(self, prev_x, prev_y, x, y):
        self.grid[prev_y][prev_x] = 0
        self.grid[y][x] = 1

    def get_board(self):
        return self.grid

    def nearby(self, x, y, name):
        for i in self.entities:
            x2, y2 = i.get_position()
            if (x == x2 - 1 or x == x2 + 1) and (y == y2 - 1 or y == y2 + 1):
                return True
        return False

    def get_entities(self):
        return self.entities

    def entity_list(self, entity):
        self.entities.append(entity)


