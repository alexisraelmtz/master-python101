#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def isTreeSymmetric(root):
    def helperTree(left, right):
        if left == None or right == None:
            return left == right
        if left.value != right.value:
            return False
        return helperTree(left.left, right.right) and helperTree(left.right, right.left)

    if root == None:
        return True
    else:
        return helperTree(root.left, root.right)
