import unittest

import board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = board.Board()

    def test_init(self):
        for x in range(7):
            for y in range(9):
                self.assertFalse(self.board.coord(x,y))

if __name__ == '__main__':
    unittest.main()
