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
    return l.next if l and l.value == k else l


l = ListNode([3, 1, 2, 3, 4, 5])
print(l)
result = removeKFromList(l, 3)
print(result)