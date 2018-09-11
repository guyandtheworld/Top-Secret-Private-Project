"""
String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
"""

import unittest


def isSubString(str1, str2):
    str2_len = len(str2)
    for i in range(len(str1) - str2_len + 1):
        if str1[i:i+str2_len] == str2:
            return True
    return False


def check_string_rotation(str1, str2):

    return isSubString(str2*2, str1)

class TestSub(unittest.TestCase):

    data = [
        ("watermelon", "erm", True),
        ("watermelon", "on", True),
        ("che guera", "e g", True),
        ("whatsuppp", "ahhaha", False)
    ]

    def test_sub_str(self):
        for data in self.data:
            assert(isSubString(*data[0:2]) == data[2])

    def test_check_string_palindrone(self):
        print(check_string_rotation("waterbottle", "erbottlewat"))


if __name__ == "__main__":
    unittest.main()
