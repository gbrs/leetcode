class Solution(object):
    def canPlaceFlowers(self, F, n):
        return sum((len(zeros) - 1) // 2 for zeros in ''.join(map(str, [0] + F + [0])).split('1')) >= n


flowerbed = [1, 0, 1, 0, 1]
n = 1

answer = Solution()

print(''.join(map(str, [0] + flowerbed + [0])).split('1'))
print(answer.canPlaceFlowers(flowerbed, n))