import unittest
import board

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = board.Piece("elephant")

    def test_init(self):
        self.assertEquals(self.piece.power, 8)
        self.assertEquals(self.piece.abilities, None)

    def test_can_kill(self):
        self.assertTrue(self.piece.can_kill(board.Piece("elephant")))
        self.assertTrue(self.piece.can_kill(board.Piece("lion")))
        
class TestPlayerPiece(unittest.TestCase):
    def setUp(self):
        self.piece = board.PlayerPiece("elephant", 0)

    def test_init(self):
        self.assertEquals(self.piece.player, 0)
        self.assertEquals(self.piece.power, 8)
        self.assertEquals(self.piece.abilities, None)

    def test_cannot_kill_same_team(self):
        own_piece = board.PlayerPiece("lion", 0)
        self.assertFalse(self.piece.can_kill(own_piece))

    def test_can_kill_other_team(self):
        enemy_piece = board.PlayerPiece("lion", 1)
        self.assertTrue(self.piece.can_kill(enemy_piece))

if __name__ == '__main__':
    unittest.main()
