class Solution(object):
    def isPalindrome(self, x):
        nums = x
        result = 0
        while nums > 0:
            last_digit = nums % 10
            result = (result * 10) + last_digit
            nums = nums // 10

        if result == x:
            return True
        else:
            return False