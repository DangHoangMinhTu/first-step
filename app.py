input_numbers = input('input numbers: ')


def read_numbers(input_nums):
    '''
    input_nums: "1,2,3,4,5"
    return: [1,2,3,4,5]
    '''
    # pass
    values = input_nums.split()
    # .split là tách 1 string thành list theo dấu cách tuy nhiên nếu mà muốn tách theo các khác thì có thể dùng kiểu "..".split(",")
    print('values: ', values)
    numbers = []
    for value in values:
        # for value in values giống kiểu
        # for (int i=0, i < len, i++){
        # value = values[i]}
        num = float(value)
        numbers.append(num)
    print('numbers is: ', numbers)
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


def get_freq_numbers(numbers):
    '''
    find values: 2
    numbers: [1,2,3,2,5,3,6,3]
    return: value -> count: [[1, 1], [2, 2], [3, 3], [5, 1], [6, 1]
    '''
    freq_numbers = []
    for number in numbers:
        found = False
        for value in freq_numbers:
            if value[0] == number:
                value[1] += 1
                found = True
        if not found:
            freq_numbers.append([number, 1])

    return freq_numbers


# input_numbers = input('input_numbers: ')

numbers = read_numbers(input_numbers)

find_value = int(input('find_value: '))


count = count_number(find_value, numbers)

print('count is: ', count)

freq_numbers = get_freq_numbers(numbers)
print('freq_numbers is: ', freq_numbers)
