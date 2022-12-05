def read_data(file_name: str) -> dict:
    with open(f'{file_name}') as f:
        lines = f.readlines()
        f.close()
    return lines


def process_data_task_1():
    data = read_data('data.txt')
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    match_score = {'L': 0, 'D': 3, 'W': 6}
    win_condition = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    lose_condition = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draw_condition = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    score = 0

    for i in data:
        split_data = i.split(' ')
        opponent = split_data[0]
        you = split_data[1].split('\n')[0]

        temp_shape = shape_score[you]
        if win_condition[opponent] == you:
            match_score = 6
        elif lose_condition[opponent] == you:
            match_score = 0
        elif draw_condition[opponent] == you:
            match_score = 3
        temp_match = match_score
        temp_score = temp_shape + temp_match
        score += temp_score
    return score


def process_data_task_2():
    data = read_data('data.txt')
    match_result = {'X': 0, 'Y': 3, 'Z': 6}
    shape = {'R': 1, 'P': 2, 'S': 3}
    rock_matches = {'X': 'S', 'Y': 'R', 'Z': 'P'}
    paper_matches = {'X': 'R', 'Y': 'P', 'Z': 'S'}
    scissor_matches = {'X': 'P', 'Y': 'S', 'Z': 'R'}
    score = 0

    for i in data:
        split_data = i.split(' ')
        opponent = split_data[0]
        match_outcome = split_data[1].split('\n')[0]
        match_points = match_result[match_outcome]
        if opponent == 'A':
            shape_score = shape[rock_matches[match_outcome]]
        elif opponent == 'B':
            shape_score = shape[paper_matches[match_outcome]]
        else:
            shape_score = shape[scissor_matches[match_outcome]]

        temp_score = match_points + shape_score
        score += temp_score
    return score

print(process_data_task_2())
