# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        ans = []

        def reversepostorder(node,level):

            if node is None:
                return
            if len(ans) == level:
                ans.append(node.val)
            if node.right:
                reversepostorder(node.right,level+1)
            if node.left:
                reversepostorder(node.left,level+1)

        reversepostorder(root,0)
        return ans
            
        

               