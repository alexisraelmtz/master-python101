n = int(input("Type the number integrers> "))


def array_addition():
    array = []
    text = input("Type the Integrers> ").split()
    items = int(len(text))
    total = int(0)
    for i in range(items):
        array.append(int(text[i]))
        total += int(text[i])
    print(array)
    print(total)
    return (array, total)


array_addition()
