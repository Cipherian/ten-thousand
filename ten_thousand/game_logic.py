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
            dice_matched = dice_counter[dice]
            if dice_matched < 3:
                total_score += GameLogic.dice_score[dice][1] * dice_matched
            elif dice_matched >= 3:
                total_score += GameLogic.dice_score[dice][3] * (dice_matched - 2)

        return total_score

    @staticmethod
    def get_scorers(dice_roll):
        dice_counter = Counter(dice_roll)
        dice_that_score = []

        for dice in dice_counter:
            if GameLogic.dice_score[dice][1] != 0:
                dice_that_score.append(dice)

        return tuple(dice_that_score)

    @staticmethod
    def validate_keepers(roll, keepers):
        roll_list = list(roll)
        for keeper in keepers:
            if keeper in roll_list:
                roll_list.remove(keeper)
            else:
                return False
        return True
