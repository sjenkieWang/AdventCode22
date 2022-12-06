from utils import read_data

def process_data_task_1():
    cont_stacks = create_container_stacks()
    movements = read_movements()
    for count, i in enumerate(movements):
        if count == 12:
            print('test')
        cont_stacks = move_crates(i, cont_stacks)
    return ''.join([j[0] if j else " " for j in cont_stacks])

def process_data_task_2():
    cont_stacks = create_container_stacks()
    movements = read_movements()
    for count, i in enumerate(movements):
        if count == 12:
            print('test')
        cont_stacks = move_n_crates(i, cont_stacks)
    return ''.join([j[0] if j else " " for j in cont_stacks])

def create_container_stacks():
    container_data = read_data('container_stacks.txt')
    stacks = [[] for i in range(len(container_data))]
    for i in range(len(container_data) - 1):
        row_i = container_data[i].split("\n")[0]
        for count, j in enumerate(range(1, len(row_i), 4)):
            if row_i[j] != " ":
                stacks[count].append(row_i[j])
    return stacks


def read_movements():
    movement_data = read_data('movements_data.txt')
    movements = []
    for i in movement_data:
        temp_data = i.split("\n")[0].split(" ")
        movements.append([int(temp_data[1]), int(temp_data[3]) - 1, int(temp_data[5]) - 1])
    return movements


def move_crates(movement: list, stacks):
    for i in range(movement[0]):
        start_column = movement[1]
        end_column = movement[2]
        if stacks[start_column]:
            container = stacks[start_column][0]
            stacks[start_column] = stacks[start_column][1:]
            stacks[end_column] = [container] + stacks[end_column]
    return stacks

def move_n_crates(movement: list, stacks):
    n_containers = movement[0]
    start_column = movement[1]
    end_column = movement[2]
    if stacks[start_column]:
        containers = stacks[start_column][:n_containers]
        stacks[start_column] = stacks[start_column][n_containers:]
        stacks[end_column] = containers + stacks[end_column]
    return stacks

print(process_data_task_2())


