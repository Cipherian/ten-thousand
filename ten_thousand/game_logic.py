from collections import Counter
import random


class GameLogic:
    dice_score = {
        1: {
            1: 100,
            3: 1000,
        },
        2: {
            1: 0,
            3: 200,
        },
        3: {
            1: 0,
            3: 300,
        },
        4: {
            1: 0,
            3: 400,
        },
        5: {
            1: 50,
            3: 500,
        },
        6: {
            1: 0,
            3: 600,
        },
    }

    @staticmethod
    def roll_dice(dice):
        number_list = []
        for num in range(dice):
            roll = random.randint(1, 6)
            number_list.append(roll)
        number_list = tuple(number_list)
        return number_list

    @staticmethod
    def calculate_score(dice_roll):
        dice_counter = Counter(dice_roll)
        total_score = 0
        dice_sum = sum(dice_counter.keys())

        if dice_sum == 21:
            return 1500

        if 2 in set(dice_counter.values()) and len(set(dice_counter.values())) == 1 and len(dice_counter.values()) == 3:
            return 1500

        for dice in dice_counter:
            number = dice_counter[dice]
            if number < 3:
                total_score += GameLogic.dice_score[dice][1] * number
            elif number >= 3:
                total_score += GameLogic.dice_score[dice][3] * (number - 2)

        return total_score


if __name__ == '__main__':
    # print('ran directly as a module')
    # print(GameLogic.calculate_score((5, 5, 5, 2, 2, 3)))
    print(GameLogic.calculate_score((2, 2, 2)))
    # to execute run: python -m ten_thousand.game_logic
    # Executing without the -m "can" have a different import structure in certain aspects when doing multiple imports
    # from different folders
