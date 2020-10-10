# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def isListPalindrome(l):
    linked = ListNode(l)
    # size = len(linked)
    # for
    if linked == linked[::-1]:
        return True
    else:
        return False


l = [0, 1, 0]
llist = ListNode(l)
print(llist)
result = isListPalindrome(llist)
print(result)