'''
Kids With the Greatest Number of Candies
There are n kids with candies. You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
'''

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

