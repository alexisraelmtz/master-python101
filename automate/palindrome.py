# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def isListPalindrome(l):
    stack = []
    c = l
    while c:
        stack.append(c.value)
        c = c.next
    while l:
        i = stack.pop()
        if l.value == i:
            l = l.next
        else:
            return False
    return True


x = [0, 1, 2, 2, 1, 0]

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(2)
node5 = ListNode(1)
node6 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


l = node1

print(f"Palindrome: {isListPalindrome(l)}")
while True:
    print(f"{l.value} ->>", end=" ")
    if l.next is None:
        print("None")
        break
    l = l.next
