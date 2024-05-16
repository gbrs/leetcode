'''
Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end of
the merged string.
Return the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        answer = []
        length1 = len(word1)
        length2 = len(word2)
        length = min(length1, length2)

        for i in range(length):
            answer.append(word1[i])
            answer.append(word2[i])

        if length1 > length2:
            answer.extend(list(word1[length:]))
        answer.extend(list(word2[length:]))

        return ''.join(answer)


'''class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """чье-то очень красивое решение.
        Срезы  позволяют не заморачиваться с проверками.
        Только конкатенацию приходится делать
        """
        return (
                ''.join(a + b for a, b in zip(word1, word2))
                + word1[len(word2):]
                + word2[len(word1):]
        )
'''

word_1 = "abcd"
word_2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(word_1, word_2))
