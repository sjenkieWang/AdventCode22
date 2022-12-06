from utils import read_data


def process_data_task_1():
    data = read_data('data.txt')
    counter = 0

    for i in data:
        temp_data = i.split(",")
        first = temp_data[0].split("-")
        first = [float(first[0]), float(first[1])]

        second = temp_data[1].split("\n")[0].split("-")
        second = [float(second[0]), float(second[1])]

        if contain_ranges(first_range=first, second_range=second):
            counter += 1
        elif contain_ranges(first_range=second, second_range=first):
            counter += 1

    return counter

def contain_ranges(first_range: list, second_range: list):
    if first_range[0] >= second_range[0] and first_range[1] <= second_range[1]:
        return True
    return False


def process_data_task_2():
    data = read_data('data.txt')
    counter = 0

    for i in data:
        temp_data = i.split(",")
        first = temp_data[0].split("-")
        first = [float(first[0]), float(first[1])]

        second = temp_data[1].split("\n")[0].split("-")
        second = [float(second[0]), float(second[1])]

        if overlap_ranges(first_range=first, second_range=second):
            counter += 1
        elif overlap_ranges(first_range=second, second_range=first):
            counter += 1

    return counter

def overlap_ranges(first_range: list, second_range: list):
    if first_range[1] >= second_range[0] and first_range[0] <= second_range[1]:
        return True
    return False

print(process_data_task_2())