from banker import calculate_bank_score
from game_logic import GameLogic


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
                    total_score = calculate_bank_score(total_score, round_score, current_round)
                    # total_score += round_score
                    # print(f'You banked {total_score} points in round {current_round}')
                    # print(f'Total score is {total_score} points')
                    current_round += 1
                # elif game_input == 'r':
                #     current_round +=1
                elif game_input == 'q':
                    play_game = False

        print(f'Thanks for playing. You earned {total_score} points')