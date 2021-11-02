# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def isListPalindromeOld(l):
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


def isListPalindrome(head):
    cache = []
    while head:
        cache.append(head.value)
        head = head.next
    for item in cache:
        verify = cache.pop()
        if item == verify:
            continue
        return False
    return True


x = [0, 1, 2, 2, 1, 0]

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(1)
node6 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


head = node1

print(f"Palindrome: {isListPalindrome(head)}")
while True:
    print(f"{head.value} ->>", end=" ")
    if head.next is None:
        print("None")
        break
    head = head.next
