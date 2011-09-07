import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.board.fresh_start()
        self.turn = 0;
        self.player = 0;
