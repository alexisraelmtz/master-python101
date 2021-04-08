# JSON: { products : [levels] }

#    p1       p2
#   /  \       |
#  L1  L2      L1


class level:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.next = None


def divider(nested):
    while nested:
        dic_Count = {}
        dic_Values = {}
        for level in nested:
            count = 0
            if level.next:
                count += 1

            else:
                break
            dic_Values[nest] = values

        return dic_Count, dic_Values
    else:
        return False


def divide(Linked_list):
    def hasLevel(product, level, count):
        if not n:
            return count
        value = n.value
        if (
            (value > low and value < high)
            and isBinary(n.left, low, n.value)
            and isBinary(n.right, n.value, high)
        ):
            return Level.next
        return False

    return isBinary(n, low, high)


# def Solve(n, low=float("-inf"), high=float("inf")):
#     def isBinary(n, low, high):
#         if not n:
#             return True
#         value = n.value
#         if (
#             (value > low and value < high)
#             and isBinary(n.left, low, n.value)
#             and isBinary(n.right, n.value, high)
#         ):
#             return True
#         return False

#     return isBinary(n, low, high)


# def isBinaryTree(n):
#     return _validator(n, float("-inf"), float("inf"))


#     4
#    / \
#   2   6
#  / \   \
# 1   3   8
