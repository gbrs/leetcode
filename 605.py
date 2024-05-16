'''
Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule
and false otherwise.
'''

'''
способ обрабатывать только тройки:
if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

Однострочник:
return sum((len(zeros) - 1) // 2 for zeros in ''.join(map(str, [0] + F + [0])).split('1')) >= n
добавил нолики по краям, сделал строку и посплитил по еденичкам.
В каждой группе ноликов по краям должны остаться нули, отальные через раз могут быть единичками
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # flowerbed == [1] корректно обрабатывается основной частью кода
        if flowerbed == [0]:
            place_count = 1
            return place_count >= n

        place_count = 0
        length = len(flowerbed)

        # обрабатываем первые два элемента, вставляя если надо единички и считая их,
        # потом тройки,
        # и в конце обрабатываем последний элемент
        if length > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            place_count += 1
            flowerbed[0] = 1

        for i in range(2, length):
            if flowerbed[i - 2] == 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                place_count += 1
                flowerbed[i - 1] = 1

        if length > 1 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
            place_count += 1
            flowerbed[length - 1] = 1

        # print(flowerbed)

        return place_count >= n


flowerbed = [0]
n = 1

answer = Solution()

print(answer.canPlaceFlowers(flowerbed, n))

