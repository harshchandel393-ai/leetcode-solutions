class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        max_index = 0

        for i in range(n):
            if i > max_index:
                return False
            max_index = max(max_index, i+nums[i])
        return True
        