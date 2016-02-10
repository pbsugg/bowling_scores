import unittest
import bowl_scorer

# class TestBowlingScore(unittest.TestCase):
#
#     def test_frame(self):
#
#     def test_score(self):
#
#     def test_complete(self):



class TestGame(unittest.TestCase):

    def test_roll(self):
        game = Game()
        rolls = 20
        game.roll(3)


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
