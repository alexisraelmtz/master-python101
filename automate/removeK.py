# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    node = l
    while node:
        if node.next and node.next.value == k:
            node.next = node.next.next
        else:
            node = node.next
    if l and l.value == k:
        return l.next
    return l


def reverse(head):
    prev = None
    while head != None:
        pointer = head.next
        head.next = prev
        prev = head
        head = pointer
    return prev


def isListPalindrome(head):
    stack = []
    pointer = head
    while pointer != None:
        stack.append(pointer.value)
        pointer = pointer.next
    while head != None:
        half = stack.pop()
        if head.value == half:
            head = head.next
        else:
            return False
    return True


x = [3, 1, 2, 3, 4]

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def traverse(l):
    while l:
        print(f"{l.value} ->>", end=" ")
        if l.next is None:
            return "None"
        l = l.next


k = 4
head = node1

print(traverse(head))

deleted = removeKFromList(head, k)
print(traverse(deleted))

node3.next = node4
inverted = reverse(head)
print(traverse(inverted))


nodeA = ListNode(8)
nodeB = ListNode(1)
nodeC = ListNode(0)
nodeD = ListNode(1)
nodeE = ListNode(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print(isListPalindrome(nodeA))