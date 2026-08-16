class Solution(object):

    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(list(subset))
            return

        elif total > target:
            return

        if index >= len(nums):
            return

        subset.append(nums[index])

        self.solve(index, total + nums[index], subset, nums, target, result)

        subset.pop()

        self.solve(index + 1, total, subset, nums, target, result)

    def combinationSum(self, candidates, target):
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result