class Solution:
    def serialize(self, root):
        if root is None:
            return "$#"

        return "$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def z_function(self, s):
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])

            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        return z

    def isSubtree(self, root, subRoot):
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)

        combined = serialized_subRoot + "|" + serialized_root

        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True

        return False