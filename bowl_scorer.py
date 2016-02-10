# Implementation of a scoring system for bowling, TDD-style
# Done quickly, but with a testing-first approach


# Rules of bowling here: http://www.pba.com/Resources/Bowling101/

# Summary:
#
# Definitions:
# "Frame" is two rolls, ex. (2,3)
# 10 frames per game
# In a given frame:
    # 1) IF not all pins are knocked down in two rolls, score for is the number of pins knocked down (roll1 + roll2).
    # 2) IF all pins are knocked down in second frame (spare), score is 10 + number knocked down in next roll (first roll of the next frame)
    # 3) IF all pins are knocked down in first roll (strike), score is 10 + number knocked down in next two rolls.
    #     This means that if you roll a strike in the final roll of the 10th frame, you get one more roll.  If you roll in strike in that frame (11th), you get a 12th as well.

# Classes
    # 1) Game--my runner file
        # two methods:
            # #roll(pins_knocked_down)--get next ball
            # score--called at end of game, to compute final score

    # 2) Frame
        # framescore--score for that frame

    # 3) Roll
        # pins--pins knocked down




# Tests


class Game:

    def __init__(self):
        pass

class Frame:

    def __init__(self):
        pass

class Roll:

    def __init__(self):
        pass
