class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        p = 0
        xx = x
        while xx > 0:
            p = p * 10 + xx % 10
            xx //= 10

        return p == x


n = 121
solution = Solution()
print(solution.isPalindrome(n))

