import math
import re

from banker import Banker, calculate_bank_score
from game_logic import GameLogic


def calculate_round_score(play_input, dice_result):
    die_selected = play_input
    round_score = 0
    dice_kept = []
    game = GameLogic()
    hot_dice = True
    first_dice = dice_result[0]
    for dice in dice_result:
        if dice != first_dice:
            hot_dice = False
    for dice in die_selected:
        try:
            dice_kept.append(int(dice))
            dice_result.remove(int(dice))
        except Exception:
            continue
    round_score += game.calculate_score(tuple(dice_kept))
    print(f'You have {round_score} unbanked points and {len(dice_result)} dice remaining')
    return round_score, tuple(dice_result), hot_dice


def welcome():
    print('Welcome to Ten Thousand'
          '\n(y)es to play or (n)o to decline')


zilch_message = """
****************************************
**        Zilch!!! Round over         **
****************************************
"""


def is_zilch(dice_results, current_round, total_score):
    if len(GameLogic.get_scorers(dice_results)) == 0:
        print(zilch_message)
        print(f"You banked 0 points in round {current_round}")
        print(f"Total score is {total_score} points")
        return True
    return False


def get_keepers(play_input):
    keepers_list = []
    for die in play_input:
        try:
            keepers_list.append(int(die))
        except Exception:
            continue
    keepers = tuple(keepers_list)
    return keepers


def has_only_strings(play_input):
    for char in play_input:
        try:
            int(char)
            return False
        except Exception:
            continue
    return True


def start_game():
    play_input = None

    welcome()
    user_input = input('> ')

    if user_input == 'n' or user_input.lower() == 'no':
        print('OK. Maybe another time')

    elif user_input.lower() == 'y' or user_input.lower() == 'yes':
        current_round = 1
        play_game = True
        total_score = 0
        dice_to_roll = 6
        hot_dice = False
        user_input_list = []
        while play_game:

            print(f'Starting round {current_round}\n'
                  f'Rolling {dice_to_roll} dice...')

            dice_results = Banker.roll_dice(dice_to_roll)

            dice_results_list = list(dice_results)
            formatted_dice_results = ''
            for i in dice_results:
                formatted_dice_results += f'{i} '

            # print(f'*** {formatted_dice_results}***')

            if is_zilch(dice_results, current_round, total_score) is True:
                current_round += 1
                continue

            cheaters = True

            while cheaters is True:

                print(f'*** {formatted_dice_results}***')
                print('Enter dice to keep, or (q)uit:')
                play_input = input('> ')

                if has_only_strings(play_input) is True:
                    print("Cheater!!! Or possibly made a typo...")
                else:
                    if GameLogic.validate_keepers(dice_results, get_keepers(play_input)) is True:
                        cheaters = False
                    else:
                        print("Cheater!!! Or possibly made a typo...")
            for dice in play_input:
                user_input_list.append(int(dice))
            # print(f"User Input List: {user_input_list}")

            if play_input.lower() == "q" or play_input.lower() == "quit":
                play_game = False
            else:
                round_score, dice_results, hot_dice = calculate_round_score(play_input, dice_results_list)
                if hot_dice is False:
                    dice_to_roll = len(dice_results)

                print('(r)oll again, (b)ank your points or (q)uit:')
                game_input = input('> ')

                if game_input.lower() == "b" or game_input.lower() == "bank":
                    total_score = calculate_bank_score(total_score, round_score, current_round)
                    if len(GameLogic.get_scorers(tuple(user_input_list))) == 6:
                        # for dice in user_input_list:
                        # if GameLogic.get_scorers(tuple(dice)) == 6:
                        print(f"User Input List=========: {user_input_list}")
                        hot_dice = True
                        dice_to_roll = 6
                        user_input_list = []
                        continue
                    current_round += 1
                elif game_input == 'r':
                    dice_to_roll = 6

                    print(f'Total score is {total_score} points')

                    current_round += 1
                    continue
                elif game_input.lower() == 'q' or game_input.lower() == "quit":
                    play_game = False

        print(f'Thanks for playing. You earned {total_score} points')


if __name__ == '__main__':
    start_game()
