// ********Fourth working day - Task 4 *********** //
import sys
from time import perf_counter

HAS_TO_HAVE = [
    'byr',  # (Birth Year)
    'ecl',  # (Eye Color)
    'eyr',  # (Expiration Year)
    'hcl',  # (Hair Color)
    'hgt',  # (Height)
    'iyr',  # (Issue Year)
    'pid',  # (Passport ID)
    # 'cid',   (Country ID)
]


def read_file(file):
    try:
        # The readlines() method returns a list containing each line in the file as a list item
        with open(file, 'r') as f:
            # content: split the string into a list of passports strings with \n\n as delimiter
            content_input = f.read().split('\n\n')
        # I used this line of code to convert in each passport string the newlines to spaces
        content_input_2 = [info.replace("\n", " ") for info in content_input]
        # My next step was to split() each passport string into a list of strings:
        content_input_3 = [string.split() for string in content_input_2]

    except:
        print('Error to read file')
        sys.exit()

    return content_input_3


def convert_to_dictionary(data_input):
    dictionary = {}
    for item in data_input:
        item_parts = item.split(":")
        key = item_parts[0]
        value = item_parts[1]
        dictionary[key] = value
    return dictionary


def find_valid_passports(data):
    count_valid_passports = 0

    for item in data:
        item_sorted = sorted(item, key=str.lower)
        items = [item for item in item_sorted if item != 'cid']

        if set(HAS_TO_HAVE) != set(items):
            continue
        count_valid_passports += 1

    return count_valid_passports


if __name__ == "__main__":
    start_timer = perf_counter()

    input_data = read_file("data.txt")
    data_to_dictionary = [convert_to_dictionary(item) for item in input_data]
    result = find_valid_passports(data=data_to_dictionary)
    print(f'Result: {result}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)
