class Solution:
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # можно было бы и рекурсивно
        t, tt, ttt = 0, 1, 1
        if n < 1:
            return 0
        if n < 3:
            return 1
        i = 3
        while i <= n:  # for легче было бы
            new = t + tt + ttt
            t, tt, ttt = tt, ttt, new
            # t, tt, ttt = tt, ttt, t + tt + ttt
            i += 1
        return ttt


s = Solution()
print(s.tribonacci(25))
