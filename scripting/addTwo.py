# Singly-linked lists are already defined with this interface:
from typing_extensions import Concatenate


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


node1 = ListNode(9876)
node2 = ListNode(5432)
node3 = ListNode(1999)
#
node4 = ListNode(1)
node5 = ListNode(8001)
#
node1.next = node2
node2.next = node3
#
node4.next = node5


def addTwoHugeNumbers(a=node1, b=node4):
    def stringer(head):
        transformed = ""
        while head:
            transformed += (str(head.value))
            head = head.next
        return int(transformed)
    cache = [stringer(item) for item in (a, b)]
    return sum(cache)


head = node1
while True:
    print(f"{head.value} ->>", end=" ")
    if head.next is None:
        print("None")
        break
    head = head.next
print(addTwoHugeNumbers())
