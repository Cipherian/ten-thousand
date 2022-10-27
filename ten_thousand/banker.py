from random import randint
import sys


def calculate_bank_score(total_score, round_score, current_round):
    total_score += round_score
    print(f'You banked {total_score} points in round {current_round}')
    print(f'Total score is {total_score} points')
    return total_score


# Banker Class
class Banker:
    """Banker is responsible for tracking points "on the shelf" and "in the bank"
    version_1
    """

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0

    # Roll Dice Statis Method (assumes import of random)
    @staticmethod
    def roll_dice(num=6):
        # version_1

        return tuple([randint(1, 6) for _ in range(num)])

    # End game Method (assumes import of sys)
    def end_game(self):
        print(f"Thanks for playing. You earned {self.balance} points")
        sys.exit()
