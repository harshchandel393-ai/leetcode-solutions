class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        original_total = (n * (n + 1)) // 2
        return original_total - sum(nums)
        