def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def mirror_values(n):
    biggest_prime = 0
    for x in range(n):
        num = int(str(x)[::-1])
        if num > biggest_prime:
            biggest_prime = num
    print(biggest_prime)
    primes = []

    for i in range(2, biggest_prime):
        if isPrime(i):
            primes.append(i)

    for j in primes:
        i_index = primes.index(j)
        j_index = int(str(i_index)[::-1])
        if j_index < len(primes):
            if isPrime(j_index) == 1:
                print(j, int(str(j)[::-1]), i_index, j_index)


mirror_values(500)
# print(mirror)
