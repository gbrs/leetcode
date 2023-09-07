class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        str1_length = len(str1)
        str2_length = len(str2)

        for divider in range(1, len(str2) + 1):
            if str2_length % divider == 0:
                length = str2_length // divider
                if str1_length % length == 0:
                    if (str2 == str2[:length] * (str2_length // length)
                            and str1 == str2[:length] * (str1_length // length)):
                        return str2[:length]

        return ""


str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

str1 = "A"
str2 = "AA"

solution = Solution()
print(solution.gcdOfStrings(str2, str1))
