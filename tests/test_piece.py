import unittest
import board

class TestPiece(unittest.TestCase):
    
    def setUp(self):
        self.piece = board.Piece("elephant")

    def test_init(self):
        self.assertEquals(self.piece.power, 8)
        self.assertEquals(self.piece.abilities, None)

    def test_can_kill(self):
        self.assertTrue(self.piece.bigger(board.Piece("elephant")))
        self.assertTrue(self.piece.bigger(board.Piece("lion")))
        
if __name__ == '__main__':
    unittest.main()

