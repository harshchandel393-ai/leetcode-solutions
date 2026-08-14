# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def solve(self, node, low, high):
        if node is None:
            return True

        if not low < node.val < high:
            return False

        left = self.solve(node.left, low, node.val)

        if left == False:
            return False

        right = self.solve(node.right, node.val, high)

        return left and right

    def isValidBST(self, root):
        return self.solve(root, float("-inf"), float("inf"))

        