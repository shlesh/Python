import random

dice_list = (1,2,3,4,5,6)
class Dice:
    def roll(self):
        print(random.choice(dice_list), random.choice(dice_list))


roller = Dice()
roller.roll()

