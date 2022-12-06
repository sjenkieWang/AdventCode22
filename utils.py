def read_data(file_name: str) -> dict:
    with open(f'{file_name}') as f:
        lines = f.readlines()
        f.close()
    return lines