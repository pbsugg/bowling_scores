import unittest
import bowl_scorer
from bowl_scorer import Game
from bowl_scorer import Roll

# class TestBowlingScore(unittest.TestCase):
#
#     def test_frame(self):
#
#     def test_score(self):
#
#     def test_complete(self):

# class TestRoll(unittest.TestCase):
#
#     def test_rollcreate(self):
#         roll = Roll()
#

class TestGame(unittest.TestCase):


    def setUp(self):
        self.game = Game()

    def test_creategame(self):
        self.assertIsInstance(self.game, Game)

    def test_rollAnAllGutterGame(self):
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score, 0)

    def test_RollAllOnes(self):
        for i in range(20):
            self.game.roll(1)
        self.assertEqual(self.game.score, 20)



#     def test_score(self):
#
# class TestFrame(unittest.TestCase):
#
#     def test_framescore(self):
#         pass
#
# class TestRoll(unittest.TestCase):
#
#     def test_pins(self):
#         pass



if __name__ == '__main__':
    unittest.main()
