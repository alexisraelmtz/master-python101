class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.data


def isListPalindrome(head):
    array = []
    pointer = head
    while pointer != None:
        array.append(pointer.value)
        pointer = pointer.next

    while head != None:
        if array.pop() == head:
            head = head.next
        return False
    return True
