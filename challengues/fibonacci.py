# answer = list(map(int, input().split()))
# start = answer[0]
# length = answer[1]

start = 1
length = 10


#def Fibo(start, length):
#    a, b = (start - 1), (start)
#    for _ in range(length):
#        print(f"{a}")
#        a, b = b, a + b

#    return a


#succesion = Fibo(start, length)
#print(succesion)

a,b = (start - 1), (start)
a, b = b, a + b
succesion = [(a for a,b in range(start:length)]
print(succesion)