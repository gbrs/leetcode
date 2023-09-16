'''
сразу вычслить один раз enough = max(candies) - extraCandies
надо было генератор списков: [i >= enough for i in candies]
'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        answer_list = []
        mx = max(candies)

        for amount in candies:
            if amount + extraCandies >= mx:
                answer_list.append(True)
            else:
                answer_list.append(False)

        return answer_list


candies = [4,2,1,1,2]
extraCandies = 1

solution = Solution()

print(*solution.kidsWithCandies(candies, extraCandies))

