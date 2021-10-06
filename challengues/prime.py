def givePosition():
    def makePrime(top):
        def isPrime(number):
            if number > 1:
                for i in range(2, number):
                    if number % i == 0:
                        return False
                return True

        primeSeq = [num for num in range(1, top) if isPrime(num)]
        return primeSeq

    myList = makePrime(100)
    for item in myList:
        position = myList.index(item) + 1
        inversePrime = int(str(item)[::-1])
        inversePos = int(str(position)[::-1])
        finalList = []
        try:
            if myList[inversePos-1] < len(myList):
                if myList[inversePos-1] == inversePrime:
                    finalList.append(
                        f"---\nPrime {item} Position #{position}\nInverted {inversePrime} Position #{inversePos}")
        except IndexError:
            print(inversePos-1, len(myList))
            pass
    return finalList


table = givePosition()
for i in table:
    print(i)
