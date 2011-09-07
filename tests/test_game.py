import unittest
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.fresh_start()

    def test_init(self):
        self.assertEquals(self.game.turn, 0)
        self.assertEquals(self.game.player, 0)

if __name__ == '__main__':
    unittest.main()
