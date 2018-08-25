"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words
"""

class Solution:
    def check_palindrome(self, str):
        letters = list(str.replace(" ", ""))
        letter_count = {}

        for letter in letters:
            if letter.lower() in letter_count:
                letter_count[letter.lower()] += 1
            else:
                letter_count[letter.lower()] = 1

        return sum(n for n in letter_count.values() if n % 2 != 0) <= 1

sol = Solution()
print(sol.check_palindrome("lamayalamy"))
