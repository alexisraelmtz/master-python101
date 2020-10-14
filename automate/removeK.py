# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    if l and l.value == k:
        return l.next
    else:
        return l


x = [3, 1, 2, 3, 4, 5]

node1 = ListNode(3)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

ll = node1
k = 3
l = removeKFromList(ll, k)
# print(l)
while True:
    print(f"{l.value} ->>", end=" ")
    if l.next is None:
        print("None")
        break
    l = l.next

#
# result = removeKFromList(l, k)
# print(result)