class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, target, subset):
            if target == 0:
                result.append(subset[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                subset.append(candidates[i])
                backtrack(i + 1, target - candidates[i], subset)
                subset.pop()

        backtrack(0, target, [])
        return result