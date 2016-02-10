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
        self.game.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_RollAllOnes(self):
        self.game.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_RollASpare(self):
        # first two rolls make spare in first frame
        self.game.roll(5)
        self.game.roll(5)
        # third roll makes not a spare
        self.game.roll(3)
        self.game.roll_many(17,0)
        self.assertEqual(self.game.score(), 16)

    def test_RollAStrike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(3)
        self.game.roll_many(16,0)
        self.assertEqual(self.game.score(), 22)



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
