class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = set(nums)
        digits = list(s.intersection([target - i for i in s]))
        # print(*digits)
        if len(digits) == 1:
            answer_1 = nums.index(digits[0])
            answer_2 = nums.index(digits[0], answer_1 + 1)
        elif len(digits) == 2:
            answer_1 = nums.index(digits[0])
            answer_2 = nums.index(digits[1])
        else:
            answer_1 = nums.index(min(digits))
            answer_2 = nums.index(max(digits))
        return [answer_1, answer_2]


lst = [3, 2, 4]
t = 6
a = Solution()
print(*a.twoSum(lst, t))

