class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        mx = sm = sum(nums[: k])
        for i in range(k, len(nums)):
            sm = sm - nums[i - k] + nums[i]
            if sm > mx:
                mx = sm
        return mx / k


# lst = [1, 12, -5, -6, 50, 3]
# width = 4
# 12.75000

lst = [-5, -5, 5, -5, 5, -5]
width = 3

answer = Solution()
print(answer.findMaxAverage(lst, width))

