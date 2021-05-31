import random


class Dice:
    def roll(self):
        one = random.randint(1, 10)
        two = random.randint(1, 10)
        return one, two


dice = Dice()
print(dice.roll())
