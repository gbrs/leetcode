'''
неправильно понял задание: максимум не среди уже просмотренных, а максимум среди всех
'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        answer_list = [True]
        max_number = candies[0]

        for amount in candies[1:]:
            if amount + extraCandies > max_number:
                answer_list.append(True)
            else:
                answer_list.append(False)
            if amount > max_number:
                max_number = amount

        return answer_list


candies = [12, 1, 12]
extraCandies = 10

solution = Solution()

print(*solution.kidsWithCandies(candies, extraCandies))

