# Singly-linked lists are already defined with this interface:
# from typing_extensions import Concatenate


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


node1 = ListNode(123)
node2 = ListNode(4)
node3 = ListNode(5)
#
node4 = ListNode(100)
node5 = ListNode(100)
node7 = ListNode(100)
# #
node1.next = node2
node2.next = node3
#
node4.next = node5
node5.next = node7


def addTwoHugeNumbers(a=node1, b=node4):
    CHUNCK = max(len(str(a.value)), len(str(b.value)))

    def stringer(head, size):
        transformed = ""
        while head:
            if len(str(head.value)) == 1:
                transformed += ((size-1)*("0") + (str(head.value)))
                head = head.next
            else:
                transformed += (str(head.value))
                head = head.next
        return int(transformed)
    cache = [stringer(item, CHUNCK) for item in (a, b)]
    ops = sum(cache)
    temp = []
    for i in range(0, len(str(ops)), CHUNCK):
        temp.append(int(str(ops)[i:i+CHUNCK]))
    return (temp)


# 12345 + 100100100
# 100112445
# Expected Output:
# [223, 104, 105]


head = node1
while True:
    print(f"{head.value} ->>", end=" ")
    if head.next is None:
        print("None")
        break
    head = head.next
print(addTwoHugeNumbers())
