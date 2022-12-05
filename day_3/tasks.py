import string


def read_data(file_name: str) -> dict:
    with open(f'{file_name}') as f:
        lines = f.readlines()
        f.close()
    return lines

def process_data():
    data = read_data('data.txt')
    lower_items = list(string.ascii_lowercase)
    upper_items = list(string.ascii_uppercase)
    lower_priorities = {lower_items[i]: i + 1 for i in range(len(lower_items))}
    upper_priorities = {upper_items[i]: i + 27 for i in range(len(upper_items))}
    sum_prio = 0

    for i in data:
        temp_data = i.split('\n')[0]
        n_items = len(temp_data)
        first_container = set(temp_data[:int(n_items/2)])
        second_container = set(temp_data[int(n_items/2):])
        shared_item = list(first_container.intersection(second_container))[0]
        if shared_item.isupper():
            temp_prio = upper_priorities[shared_item]
        else:
            temp_prio = lower_priorities[shared_item]

        sum_prio += temp_prio
    return sum_prio

def process_data_task_2():
    data = read_data('data.txt')
    lower_items = list(string.ascii_lowercase)
    upper_items = list(string.ascii_uppercase)
    lower_priorities = {lower_items[i]: i + 1 for i in range(len(lower_items))}
    upper_priorities = {upper_items[i]: i + 27 for i in range(len(upper_items))}
    sum_prio = 0

    for i in range(0, len(data), 3):
        first_bag = set(data[i].split('\n')[0])
        second_bag = set(data[i + 1].split('\n')[0])
        third_bag = set(data[i + 2].split('\n')[0])

        temp_shared = first_bag.intersection(second_bag)
        shared_item = list(temp_shared.intersection(third_bag))[0]
        if shared_item.isupper():
            temp_prio = upper_priorities[shared_item]
        else:
            temp_prio = lower_priorities[shared_item]

        sum_prio += temp_prio
    return sum_prio

print(process_data_task_2())
