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


def calculate_round_score(play_input, dice_results_list):
    die_selected = play_input
    round_score = 0
    die_selected_list = []
    for dice in die_selected:
        die_selected_list.append(int(dice))
        dice_results_list.remove(int(dice))
    round_score += game.calculate_score(tuple(die_selected_list))
    print(f'You have {round_score} unbanked points and {len(dice_results_list)} dice remaining')
    return round_score, tuple(dice_results_list)

if __name__ == '__main__':
    print('Welcome to Ten Thousand'
          '\n(y)es to play or (n)o to decline')
    user_input = input('> ')

    if user_input == 'n':
        print('OK. Maybe another time')

    elif user_input == 'y':
        current_round = 1
        play_game = True
        total_score = 0
        while play_game:
            print(f'Starting round {current_round}\n'
                  'Rolling 6 dice...')
            game = GameLogic()
            dice_results = game.roll_dice(6)
            dice_results_list = list(dice_results)
            formatted_number = ''
            for i in dice_results:
                formatted_number += f'{i} '
            print(f'*** {formatted_number}***')
            print('Enter dice to keep, or (q)uit:')
            play_input = input('> ')
            if play_input == "q":
                play_game = False
            else:
                round_score, dice_results = calculate_round_score(play_input, dice_results_list)
                print('(r)oll again, (b)ank your points or (q)uit:')
                game_input = input('> ')

                if game_input == "b":
                    total_score += round_score
                    print(f'You banked {total_score} points in round {current_round}')
                    print(f'Total score is {total_score} points')
                    current_round += 1
                # elif game_input == 'r':
                #     current_round +=1
                elif game_input == 'q':
                    play_game = False


        print(f'Thanks for playing. You earned {total_score} points')

