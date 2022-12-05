
def read_data(file_name: str) -> dict:
    with open(f'{file_name}') as f:
        lines = f.readlines()
        f.close()
    return lines


def process_data():
    data = read_data('data.txt')
    temp_snacks = []
    first = 0
    second = 0
    third = 0
    all_calories = []

    for i in data:
        calories = i.split('\n')[0]
        if calories:
            temp_snacks.append(float(calories))
        else:
            total_cals = sum(temp_snacks)
            all_calories.append(total_cals)
            temp_snacks = []
            print(total_cals)
            if total_cals > first:
                first = total_cals
            elif total_cals > second:
                second = total_cals
            elif total_cals > third:
                third = total_cals
    calories = sum([first, second, third])
    return calories



def sum_calories():
    print(process_data())
    pass


sum_calories()


def process_data():
    data = read_data('data.txt')
    lower_items = list(string.ascii_lowercase)
    upper_items = list(string.ascii_uppercase)
    lower_priorities = {lower_items[i]: i + 1 for i in range(len(lower_items))}
    upper_priorities = {upper_items[i]: i + 27 for i in range(len(upper_items))}
    sum_prio = 0

    for i in range(len(data)):
        sum_three_prio = 0
        for j in range(i, i + 3, 1):
            temp_data = data[i].split('\n')[0]
            n_items = len(temp_data)
            first_container = set(temp_data[:int(n_items/2)])
            second_container = set(temp_data[int(n_items/2):])
            shared_item = list(first_container.intersection(second_container))[0]
            if shared_item.isupper():
                temp_prio = upper_priorities[shared_item]
            else:
                temp_prio = lower_priorities[shared_item]

            sum_three_prio += temp_prio
        sum_prio += sum_three_prio
    return sum_prio