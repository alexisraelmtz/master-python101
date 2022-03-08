
from json.encoder import INFINITY


left, down, right, up = 1, 2, 3, 4

# left front right
directions = [left, down, right, up]


def is_flat(lot, loc):
    x, y = loc
    return lot[y][x] == 1


def is_obstacle(lot, loc):
    x, y = loc
    return lot[y][x] == 9


def is_trench(lot, loc):
    x, y = loc
    return lot[y][x] == 0


def move(loc, direction):
    x, y = loc
    if direction == left:
        return (x-1, y)
    if direction == right:
        return (x+1, y)
    if direction == down:
        return (x, y+1)
    if direction == up:
        return (x, y-1)


def move_back(loc, direction):
    x, y = loc
    if direction == left:
        return (x+1, y)
    if direction == right:
        return (x-1, y)
    if direction == down:
        return (x, y-1)
    if direction == up:
        return (x, y+1)


def is_valid(lot, loc):
    x, y = loc
    if x < 0 or x > len(lot[0])-1:
        return False
    if y < 0 or y > len(lot)-1:
        return False
    if is_trench(lot, loc):
        return False
    return True


def main():

    shortest_path = INFINITY
    path = []
    # X, Y
    loc = (0, 0)
    if is_obstacle(lot, loc):
        return 0
    last_loc_invalid = False
    last_direction = 0
    count = 0
    visited = set([])

    while True:
        count += 1
        if count > 20:
            break
        direction = 0
        for direction in directions[last_direction::]:
            new_loc = move(loc, direction)
            if not is_valid(lot, new_loc) or new_loc in visited:
                last_loc_invalid = True
                continue

            path.append(direction)
            last_loc_invalid = False
            loc = new_loc
            visited.add(loc)

            print(direction, loc, path, is_flat(lot, loc))
            if is_obstacle(lot, loc):
                last_loc_invalid = True
            if is_obstacle(lot, loc) and len(path) < shortest_path:
                print('obstacle')
                shortest_path = len(path)
            break

        if last_loc_invalid and direction == up:
            last_direction = path.pop()
            if len(path) == 0:
                break
            loc = move_back(loc, last_direction)
            direction = last_direction

    print(path)
    print(shortest_path)


if __name__ == '__main__':

    lot = [
        [1, 0, 0, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 9]
    ]

    main()
