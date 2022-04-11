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


def pattern_search(sequence, pattern):
    positions = set()
    index = 0
    while index < len(sequence) - len(pattern):
        if sequence[index:index + len(pattern)] == pattern:
            positions.add(index)
        index = index + 1
    return positions

def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while left < right:
        middle = (left + right) // 2
        if sequence[middle] == number:
            return middle
        elif sequence[middle] < number:
            left = middle +1
        elif sequence[middle] > number:
            right = middle - 1
    return None



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, number))
    linear_data = read_data("sequential.json", "dna_sequence")
    print(linear_data)
    print(pattern_search(linear_data, pattern))
    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    print(binary_search(ordered_numbers, number))



if __name__ == '__main__':
    number = 9
    pattern = "GGT"
    main()