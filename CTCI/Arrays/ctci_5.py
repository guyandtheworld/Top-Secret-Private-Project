"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""

class Solution:
    def check_edit(self, str1, str2):
        strlen1 = len(str1)
        strlen2 = len(str2)
        edit_bit = []
        if strlen1 == strlen2:
            for i in range(strlen1):
                if str1[i] != str2[i]:
                    edit_bit.append(0)
        elif strlen1 > strlen2:
            for i in range(strlen2):
                if str1[i] != str2[i]:
                    edit_bit.append(0)
                    break
            if str1[strlen1 - 1] != str2[strlen2 - 1]:
                edit_bit.append(0)
        else:
            for i in range(strlen1):
                if str1[i] != str2[i]:
                    edit_bit.append(0)
                    break
            if str1[strlen1 - 1] != str2[strlen2 - 1]:
                edit_bit.append(0)
        return len(edit_bit) == 1


    # Too cluttered. Split code to functions
    # It's only one edit always. So break away when the edit is encountered.
    # Using while loop, you could get rid of the edge end condition

sol = Solution()
print(sol.check_edit("pale", "pale"))
