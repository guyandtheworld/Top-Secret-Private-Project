"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

class Solution:
    def shorten_string(self, string):
        index_table = {}
        char_list = []
        prev = ""
        for i in string:
            if prev != i:
                char_list.append(i)
                index_table[len(char_list) - 1] = 1
                prev = i
            else:
                index_table[len(char_list) - 1] += 1

        res = ""
        for i, val in enumerate(char_list):
            res += val + str(index_table[i])
        return res

#
# sol = Solution()
# print(sol.shorten_string("aabcccccaaa"))

import unittest


def string_compression(string):
    compressed = []
    counter = 1

    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            compressed.append(string[i-1] + str(counter))
            counter = 0
        counter += 1

    compressed.append(string[i-1] + str(counter))
    return min(string, "".join(compressed), key=len)


class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compressed(self):
        for d in self.data:
            assert string_compression(d[0]), d[1]


if __name__ == "__main__":
    unittest.main()