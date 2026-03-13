input_numbers = input('input numbers: ')


def read_numbers(input_nums):
    '''
    input_nums: "1,2,3,4,5"
    return: [1,2,3,4,5]
    '''
    # pass
    values = input_nums.split()
    print('values: ', values)
    numbers = []
    for value in values:
        num = float(value)
        numbers.append(num)
    print(numbers)
    return numbers


def count_number(find_value, numbers):
    '''
    find_value: 2
    number: [1,2,3,4,5}
    return: 2
    '''
    # pass
    count = 0
    for value in numbers:
        if value == find_value:
            count += 1
    return count

# [1, 1], [2, 2], [3, 3], [5, 1], [6, 1]


def get_freq_numbers():
    '''
    find values: 2
    numbers: [1,2,3,2,5,3,6,3]
    return: value -> count: [[1, 1], [2, 2], [3, 3], [5, 1], [6, 1]
    '''
    freq_numbers = []
    for number in numbers:
        found = False
        for values in freq_numbers:
            if values[0] == number:
                values[1] += 1
                found = True
        if not found:
            freq_numbers.append([number, 1])

    return freq_numbers


# input_numbers = input('input_numbers: ')
input_numbers = "1 2 3 4 5"
numbers = read_numbers(input_numbers)
print('numbers: ', numbers)

find_value = 3
count = count_number(find_value, numbers)

print(count)

freq_nubers = get_freq_numbers()
