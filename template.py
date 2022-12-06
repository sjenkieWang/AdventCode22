def read_data(file_name: str) -> dict:
    with open(f'{file_name}') as f:
        lines = f.readlines()
        f.close()
    return lines


def process_data():
    data = read_data('container_stacks.txt')

    for i in data:
        temp_data = i.split(",")

    pass

print(process_data())