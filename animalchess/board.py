class Board:
    WIDTH, LENGTH = 7, 9

    def __init__(self):
        self.grid = []
        for x in xrange(7):
            row = []
            for y in xrange(9):
                row.append(None)
            self.grid.append(row)

    def coord(self, x,y):
        return self.grid[x][y]
