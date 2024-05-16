'''
Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

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
