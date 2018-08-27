"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""

class Solution:
    def check_modify_helper(self, str1, str2):
        diff = False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if diff:
                    return False
                else:
                    diff = True
        return diff

    def check_edit_helper(self, str1, str2):
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                if i != j:
                    return False
                else:
                    j+=1
            else:
                i += 1; j += 1
        return True

    def check_edit(self, str1, str2):
        strlen1 = len(str1)
        strlen2 = len(str2)
        if strlen1 == strlen2:
            return self.check_modify_helper(str1, str2)
        elif strlen1 + 1 == strlen2:
            return self.check_edit_helper(str1, str2)
        elif strlen1 - 1 == strlen2:
            return self.check_edit_helper(str2, str1)
        return False


    # Too cluttered. Split code to functions
    # It's only one edit always. So break away when the edit is encountered.
    # Using while loop, you could get rid of the edge end condition

sol = Solution()
print(sol.check_edit("pale", "pals"))
