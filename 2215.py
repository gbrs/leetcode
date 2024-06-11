class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)
        answer.append(list(set1 - set2))
        answer.append(list(set2 - set1))
        return answer


# lst_1 = [1, 2, 3]
# lst_2 = [2, 4, 6]
# [[1,3],[4,6]]

lst_1 = [1, 2, 3, 3]
lst_2 = [1, 1, 2, 2]
# [[3], []]

s = Solution()
print(s.findDifference(lst_1, lst_2))

