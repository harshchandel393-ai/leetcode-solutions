class Solution(object):
    def reverse(self, x):
        nums = abs(x)
        rev = 0

        while nums > 0:
            last_digit = nums % 10
            rev = (rev * 10) + last_digit
            nums = nums // 10

        if x < 0:
            rev = -rev

        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev