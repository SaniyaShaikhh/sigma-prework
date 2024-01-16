def user_input():
    user_input = input("Enter a list of integers (separated by a comma): ")
    list = [int(number) for number in user_input.split(",")]
    return list


def check_number(numbers, current_min, current_max):
    for number in numbers:
        if number >= current_max:
            current_max = number
        elif number < current_min:
            current_min = number
    return current_min, current_max


numbers = user_input()
current_max = numbers[0]
current_min = numbers[0]
current_min, current_max = check_number(numbers, current_min, current_max)
maxmin = [current_min, current_max]
print(maxmin)
