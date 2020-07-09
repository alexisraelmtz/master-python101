numbers = (5, 2, 5, 2, 2, 5, 9, 3, 5, 5, 2, 6, 2, 8, 1)
individuales = []

for number in numbers:
    iteration = ""
    for rep in range(number):
        iteration += "X"
    print(iteration)

for number in numbers:
    if number not in individuales:
        individuales.append(number)

individuales.sort()
print(individuales)


"""
for number in numbers:
    print(f"X" * (number))
"""
