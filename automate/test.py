w = [3, 0, 5, 2, 6, 0, 7, 8, 0]
for n in range(len(w)):
    if w[n] == 0:
        n += 1
    else:
        print(w[n])
