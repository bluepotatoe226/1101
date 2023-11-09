def read_numbers(one_hundred):
    numbers = []
    with open(one_hundred, 'r') as file:
        for line in file:
            number = (line.strip())
            numbers.append(number)
    return numbers
        
def missing_numbers(numbers):
    numset = set(numbers)
    missing_numbers = []
    for num in range(1,101):
        if num not in numset:
            missing_numbers.append(num)
    return missing_numbers

def write_numbers(numbers, one_hundred):
    with open(one_hundred, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

numbers = read_numbers('one_hundred.txt')

missing_numbers = missing_numbers(numbers)

missing_numbers.sort()

write_numbers(missing_numbers, 'one_hundered_sorted.txt')

print('Missing numbers are written in the one_hundred_sorted.txt file')

