class Solution:
    diameter = 0

    def calculateHeight(self, root):
        if not root:
            return 0

        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)

        self.diameter = max(self.diameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.calculateHeight(root)
        return self.diameter