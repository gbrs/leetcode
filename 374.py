# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n + 1
        while left < right:
            middle = (left + right) // 2
            if guess(middle) == -1:
                right = middle
            elif guess(middle) == 1:
                left = middle
            else:
                return middle
        return left


def guess(x):
    if x < pick:
        return 1
    if x > pick:
        return -1
    return 0


s = Solution()
number = 2
pick = 2
print(s.guessNumber(number))
