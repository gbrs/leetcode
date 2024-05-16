class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        left = 0
        right = n - 1

        # левый флаг на первый ноль, правый туда же
        while left < n and nums[left] != 0:
            left += 1
        right = left

        # смещаем правый флаг на ближайший не ноль, свапаемся, смещаем левый флаг на правый
        while right < n - 1 and left < n - 1:
            while right < n - 1 and nums[right] == 0:
                right += 1
            nums[left], nums[right] = nums[right], nums[left]
            while left < n and nums[left] != 0:
                left += 1

        return nums


lst = [0, -4, 0, 1, 0, 12, 3]
lsts = Solution()
lst_2 = lsts.moveZeroes(lst)
print(lst_2)
lst_3 = [-4, 1, 12, 3, 0, 0, 0]
print(lst_3 == lst_2)
