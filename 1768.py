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


word_1 = "abcd"
word_2 = "pqrs"
solution = Solution()
print(solution.mergeAlternately(word_1, word_2))
