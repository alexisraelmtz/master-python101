def dynamicArray(n, queries):
    ans = []
    last = 0
    z = n[0]
    arr = [[] for _ in range(z)]
    for query in queries:
        ty = query[0]
        x = query[1]
        y = query[2]
        i = (x ^ last) % z
        if ty == 1:
            arr[i].append(y)
        else:
            last = arr[i][y % (len(arr[i]))]
            ans.append(last)
    return ans


n = [2, 5]
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

print(queries)

A = dynamicArray(n, queries)
print("\n".join(map(str, A)))
