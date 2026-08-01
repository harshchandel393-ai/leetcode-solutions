class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        cur_Max = 1
        cur_Min = 1

        for n in nums:
            if n ==0:
                cur_Max = 1
                cur_Min = 1
                continue
            
            temp = n*cur_Max
            cur_Max = max(n*cur_Max, n*cur_Min, n)
            cur_Min = min(temp, n*cur_Min, n)
            res = max(res, cur_Max)
        return res        