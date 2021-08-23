def find_all_hobbyists(hobby, hobbies):
    results = []
    for player, sports in hobbies.items():
        print(player, sports)
        if hobby in sports:
            results.append(player)
    return results


hobbies = {
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets', 'Yoga'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

# print(f"Hi, {hobbies.items()}")

print(find_all_hobbyists('Yoga', hobbies))


def find_unique_numbers(numbers):
    # unique = set(numbers)
    # for num in numbers:
    #     if numbers.count(num) < 1:
    #         unique.
    numbers.sort()
    new = {}
    for num in (numbers):
        new[num] = new.get(num, 0) + 1
    res = [i for i in new.keys() if new[i] == 1]
    return res


print(find_unique_numbers([1, 2, 1, 3, 3, 3]))


def tuple_slice(startIndex, endIndex, tup):
    new = tup[startIndex:endIndex]
    new = [str(i) for i in new]
    return ",".join(new)
    #  ",".join(tup[int(startIndex):int(endIndex)])


print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))
