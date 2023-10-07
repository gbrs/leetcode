'''
красивые решения:
- обмен в списке через два указателя
- re.sub()
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = 'aoiueAOIUE'
        vowel_list = [char for char in s if char in vowels]
        answer = []

        for char in s:
            if char in vowels:
                answer.append(vowel_list.pop())
            else:
                answer.append(char)

        return ''.join(answer)


solution = Solution()
string = 'lEetcode'

print(solution.reverseVowels(string))
