# def hasPathWithGivenSum(root, s):
#     def tree_sum(root):
#         while root == None:
#             return 0
#         yield  root.value + tree_sum(root.left) + tree_sum(root.right)

#     # yield every path and check value?

#     added_tree = tree_sum(root)
#     while added_tree is not None:
#         if added_tree == s:
#             return True
#     return False


def hasPathWithGivenSum_two(t, s):
    if t is None:
        return s == 0

    return hasPathWithGivenSum(t.left, s - t.value) or hasPathWithGivenSum(
        t.right, s - t.value
    )


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def hasPathWithGivenSum(root, target):
    if root == None:
        return False
    if root.left == None and root.right == None and target - root.value == 0:
        return True
    else:
        return hasPathWithGivenSum(
            root.left, target - root.value
        ) or hasPathWithGivenSum(root.right, target - root.value)
