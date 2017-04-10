class Solution(object):
    def reverse(self, x):
        negative = False
        if x < 0:
            negative = True
            x = 0 - x
        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        if result >= 2 ** 31:
            return 0
        if negative:
            result = 0 - result
        return result
        """
        :type x: int
        :rtype: int
        """
