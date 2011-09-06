import animal_exceptions

DATA = [["elephant", 8, None],
        ["lion",7,"jumps"],
        ["rat",1,"swims"]]

RULES = {}
for d in DATA:
    RULES[d[0]] = {"power":d[1], "abilities":d[2]}

class Board:
    WIDTH, LENGTH = 7, 9

    def __init__(self):
        self.grid = []
        self.pieces = {}
        self.special = {}
        for x in xrange(7):
            row = []
            for y in xrange(9):
                row.append(None)
            self.grid.append(row)

    def coord(self, x,y):
        return self.grid[x][y]
    
    def place(self, piece, position):
        if self.coord(*position):
            raise animal_exceptions.ReplaceException(position)
        else:
            x,y = position
            self.grid[x][y] = piece
            self.pieces[piece] = Piece(piece)

    def place_tile(self, tile_type, position):
        if tile_type not in self.special:
            self.special[tile_type] = set()
        self.special[tile_type].add(position)

    def tile_is(self, tile_type, position):
        try:
            return position in self.special[tile_type]
        except KeyError:
            return False
    
    def destroy(self, position):
        x,y = position
        self.grid[x][y] = None

    def water_in_between(self, start, finish):
        if start == finish:
            return False

        elif start[0] == finish[0]:
            between_tiles = [(start[0],y) for y in xrange(min(start[1],finish[1])+1, max(start[1],finish[1]))]
            between_tiles = [self.tile_is("water", tile) for tile in between_tiles]
            if between_tiles:
                return all(between_tiles)
            else:
                 return False
        elif start[1] == finish[1]:
            between_tiles = [(x,start[1]) for x in xrange(min(start[0],finish[0]+1), max(start[0],finish[0]))]
            between_tiles = [self.tile_is("water", tile) for tile in between_tiles]
            if between_tiles:
                return all(between_tiles)
            else:
                return False
        else:
            return False

    def can_move(self, start, finish):
        if start == finish:
            return False
        mover = self.pieces[self.coord(*start)]
        if not mover:
            return False
        if self.tile_is("water", finish) and mover.abilities != "swims":
            return False
        if mover.abilities != "jumps" and self.water_in_between(start,finish):
            return False
        target = self.coord(*finish)
        if target and not mover.bigger(self.pieces[target]):
            return False
        return True
    
    def move(self, start, finish):
        if self.can_move(start, finish):
            self.destroy(finish)
            mover = self.pieces[self.coord(*start)]
            self.place(mover.name, finish)
            self.destroy(start)
            
class Piece:
    def __init__(self, name):
        self.name = name
        self.power = RULES[name]["power"]
        self.abilities = RULES[name]["abilities"]

    def bigger(self, opponent):
        return self.power >= opponent.power
