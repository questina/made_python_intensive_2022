import random


def generate_tests_input():
    win_combinations = {
        "row": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "column": [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        "diag": [[1, 5, 9], [3, 5, 7]]
    }
    test = []
    for comb_place in win_combinations:
        for comb in win_combinations[comb_place]:
            comb_test = [comb_place]
            left_digits = [i for i in range(1, 10) if i not in comb]
            random.shuffle(left_digits)
            while sorted(left_digits[:3]) in win_combinations[comb_place]:
                random.shuffle(left_digits)
            comb_test.append(comb)
            comb_test.append(left_digits)
            test.append(comb_test)
    return test


def combine_strategies(first_player_strategy, second_player_strategy, input_steps):
    for first_strategy, second_strategy in zip(first_player_strategy, second_player_strategy):
        input_steps.append(str(first_strategy))
        input_steps.append(str(second_strategy))
    if len(first_player_strategy) == len(second_player_strategy) + 1:
        input_steps.append(str(first_player_strategy[-1]))
    return input_steps
