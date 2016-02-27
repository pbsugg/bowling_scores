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
        self.rolls = []

    def roll(self, number_to_roll):
        self.rolls.append(number_to_roll)

    def roll_many(self, number_of_rolls, pins):
        for i in range(number_of_rolls):
            self.roll(pins)

    def score(self):
        score = 0
        frame = 0
        first_in_frame = 0
        while frame < 10:
            if self.strike(first_in_frame):
                score += (10 + self.bonus_for_strike(first_in_frame))
                first_in_frame += 1
            elif self.spare(first_in_frame):
                score += 10 + self.rolls[first_in_frame + 2]
                first_in_frame += 2
            else:
                score += self.rolls[first_in_frame] + self.rolls[first_in_frame + 1]
                first_in_frame += 2
            frame += 1
            print(score)
        return score

    def bonus_for_strike(self, first_in_frame):
        next_two_rolls_score = (self.rolls[first_in_frame + 1]
                                + self.rolls[first_in_frame + 2]    
                                )
        return next_two_rolls_score

    def strike(self, first_in_frame):
        return self.rolls[first_in_frame] == 10

    def spare(self, first_in_frame):
        return self.rolls[first_in_frame] + self.rolls[first_in_frame + 1] == 10

class Frame:

    def __init__(self):
        pass

class Roll:

    def __init__(self):
        pass
