def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


# numbers = [5, 9, 2, 8, 7, 13, 93, 2, 4]
# print(find_max(numbers))

