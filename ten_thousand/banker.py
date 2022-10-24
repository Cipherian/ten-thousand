def calculate_bank_score(total_score, round_score, current_round):
    total_score += round_score
    print(f'You banked {total_score} points in round {current_round}')
    print(f'Total score is {total_score} points')
    return total_score
