class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = height = 0
        for h in gain:
            height += h
            highest = max(highest, height)
        return highest


sol = Solution()

# lst = [-4, -3, -2, -1, 4, 3, 2]
# 0

lst = [-5, 1, 5, 0, -7]
# 1

print(sol.largestAltitude(lst))
