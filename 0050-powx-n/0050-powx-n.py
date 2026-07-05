class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1.0 / x
            n = -n

        ans = 1.0

        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return ans