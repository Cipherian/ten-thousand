from banker import calculate_bank_score
from game_logic import GameLogic


def calculate_round_score(play_input, dice_results_list):
    die_selected = play_input
    round_score = 0
    die_selected_list = []
    game = GameLogic()
    for dice in die_selected:
        die_selected_list.append(int(dice))
        dice_results_list.remove(int(dice))
    round_score += game.calculate_score(tuple(die_selected_list))
    print(f'You have {round_score} unbanked points and {len(dice_results_list)} dice remaining')
    return round_score, tuple(dice_results_list)

def welcome():
    print('Welcome to Ten Thousand'
          '\n(y)es to play or (n)o to decline')

def start_game():
    welcome()
    user_input = input('> ')

    if user_input == 'n' or user_input.lower() == 'no':
        print('OK. Maybe another time')

    elif user_input.lower() == 'y' or user_input.lower() == 'yes':
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
            if play_input.lower() == "q" or play_input.lower() == "quit":
                play_game = False
            else:
                round_score, dice_results = calculate_round_score(play_input, dice_results_list)
                print('(r)oll again, (b)ank your points or (q)uit:')
                game_input = input('> ')

                if game_input.lower() == "b" or game_input.lower() == "bank":
                    total_score = calculate_bank_score(total_score, round_score, current_round)
                    print(f'You banked {total_score} points in round {current_round}')
                    print(f'Total score is {total_score} points')
                    current_round += 1
                elif game_input == 'r':
                    current_round +=1
                    continue
                elif game_input.lower() == 'q' or game_input.lower() == "quit":
                    play_game = False
        print(f'Thanks for playing. You earned {total_score} points')

if __name__ == '__main__':

    start_game()


