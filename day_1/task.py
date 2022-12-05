
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