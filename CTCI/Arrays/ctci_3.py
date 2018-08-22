"""Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string"""

class Solution:
    def convert_string(self, str, space):
        return str.replace(" ", "%20")


sol = Solution()
print(sol.convert_string("Mr John Smith", 13))
