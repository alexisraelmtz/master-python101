input1 = list(input().strip().split(":"))

# print(input1)
a = int(input1[0])
b = int(input1[1])
c = int(input1[2][0:2])
d = input1[2][2:4]


while 1 <= a <= 12 and 00 <= b <= 59 and 00 <= c <= 59:
    # while b >= 00 and b <= 59:
    if d.upper() == "AM":
        if a == 12:
            print(f"{a-12:02d}:{b:02d}:{c:02d}")
            break
        else:
            print(f"{a:02d}:{b:02d}:{c:02d}")
            break
    elif d.upper() == "PM":
        if a == 12:
            print(f"{a:02d}:{b:02d}:{c:02d}")
            break
        else:
            print(f"{(a + 12):02d}:{b:02d}:{c:02d}")
            break
    else:
        break
    break

# print(f"{}:{}:{}")
