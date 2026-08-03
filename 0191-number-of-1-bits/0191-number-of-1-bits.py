class Solution(object):
    def hammingWeight(self, n):
        res = 0 
        while n:
            n = n & (n-1)
            res = res + 1
        return res
        
        