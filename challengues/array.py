n = int(input("Type the number of elements> "))
text = input("Type the elements> ").split()


def array_addition():
    array = []
    total = int(0)
    for i in range(n):
        individual = int(text[i])
        array.append(individual)
        total += individual
    print(array)
    print(total)


array_addition()
