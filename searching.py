import os
import json

# get current working directory path
cwd_path = os.getcwd()



def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
        if field not in set(data.keys()):
            return None
    return data[field]

def linear_search(data, number):
    count = 0
    positions = []

    for idx, num in enumerate(data):
        if num == number:
            positions.append(idx)
            count += 1
            number_count = {"index:": positions, "Pocet:": count}
    return number_count



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    number_count = linear_search(sequential_data, number)
    print(sequential_data)
    print(number_count)


if __name__ == '__main__':
    number = 9
    main()