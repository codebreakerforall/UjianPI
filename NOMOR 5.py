def read_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers

def format_number(number):
    return format(number, ',').replace(',', 'X').replace('X', ',')

if __name__ == '__main__':
    numbers = read_numbers('input.txt')
    total = sum(numbers)
    print(f'The sum of the numbers is {format_number(total)}')