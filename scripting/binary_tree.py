class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def Solve(n, low=float("-inf"), high=float("inf")):
    def isBinary(n, low, high):
        if not n:
            return True
        value = n.value
        if (
            (value > low and value < high)
            and isBinary(n.left, low, n.value)
            and isBinary(n.right, n.value, high)
        ):
            return True
        return False

    return isBinary(n, low, high)

    # def isBinaryTree(n):
    #     return _validator(n, float("-inf"), float("inf"))


#     4
#    / \
#   2   6
#  / \   \
# 1   3   8


n1 = Node(4)
n2 = Node(2)
n3 = Node(6)
n4 = Node(1)
n5 = Node(3)
n6 = Node(8)

n1.right = n3
n1.left = n2
n2.right = n5
n2.left = n4
n3.right = n6

print(Solve(n1))


#     5
#    / \
#   4   7
#      / \
#     2#6   8


n1 = Node(5)
n2 = Node(4)
n3 = Node(7)
n4 = Node(6)  # 2 False
n5 = Node(8)

n1.right = n3
n1.left = n2
n3.left = n4
n3.right = n5

print(Solve(n1))
