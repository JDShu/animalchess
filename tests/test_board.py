import unittest

import board, animal_exceptions

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = board.Board()

    def test_init(self):
        for x in range(7):
            for y in range(9):
                self.assertFalse(self.board.coord(x,y))

    def test_place_piece(self):
        self.board.place("elephant",(0,0))
        self.assertEquals(self.board.coord(0,0), "elephant")

    def test_place_again(self):
        with self.assertRaises(animal_exceptions.ReplaceException):
            self.board.place("elephant",(0,0))
            self.board.place("rat",(0,0))

    def test_move(self):
        self.board.place("elephant",(0,0))
        self.board.move((0,0),(0,1))
        self.assertEquals(self.board.coord(0,0), None)
        self.assertEquals(self.board.coord(0,1), "elephant")

    def test_capture(self):
        self.board.place("elephant",(0,0))
        self.board.place("lion",(0,1))
        self.board.move((0,0),(0,1))
        self.assertEquals(self.board.coord(0,1), "elephant")

    def test_capture_fail(self):
        self.board.place("elephant",(0,0))
        self.board.place("lion",(0,1))
        self.board.move((0,1),(0,0))
        self.assertEquals(self.board.coord(0,0), "elephant")
        self.assertEquals(self.board.coord(0,1), "lion")

    def test_terrain(self):
        self.board.place_tile("water", (0,0))
        self.assertTrue(self.board.tile_is("water", (0,0)))

    def test_swimmer(self):
        self.board.place_tile("water", (0,0))
        self.board.place("rat", (0,1))
        self.board.move((0,1),(0,0))
        self.assertEquals(self.board.coord(0,0), "rat")
        self.assertEquals(self.board.coord(0,1), None)
        
    def test_nonswimmer(self):
        self.board.place_tile("water", (0,0))
        self.board.place("elephant", (0,1))
        self.board.move((0,1),(0,0))
        self.assertEquals(self.board.coord(0,0), None)
        self.assertEquals(self.board.coord(0,1), "elephant")

    def test_jumper(self):
        self.board.place_tile("water", (0,1))
        self.board.place("lion",(0,0))
        self.board.move((0,0),(0,2))
        self.assertEquals(self.board.coord(0,0), None)
        self.assertEquals(self.board.coord(0,2), "lion")

    def test_non_jumper(self):
        self.board.place_tile("water",(0,1))
        self.board.place("elephant",(0,0))
        self.board.move((0,0),(0,2))
        self.assertEquals(self.board.coord(0,0), "elephant")
        self.assertEquals(self.board.coord(0,2), None)

        
if __name__ == '__main__':
    unittest.main()
