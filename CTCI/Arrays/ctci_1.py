"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


class CheckUniqueStrings:
    def check_string_conventional(self, string):
        for i, char in enumerate(string):
            if char in string[:i] or char in string[i+1:]:
                return False
        return True

    def check_string_hash(self, string):
        table = {}
        for letter in string:
            if letter in table:
                return False
            table[letter] = True
        print(table)
        return True

    """The recommended algorithm checks only for ASCII
    * Create a 128 bit long Bool array. (Since only 128 characters exists for ASCII.)
    * Set the value of that character in the array to be True if exists
    * Return false if the array has True in the i-th position.
    """
    def check_string_ascii(self, string):
        if len(string) > 128:
            return False

        bool_array = {}

        for i in string:
            val = ord(i)
            if val in bool_array:
                return False
            bool_array[val] = True
        return True


obj = CheckUniqueStrings()
# print(obj.check_string_conventional("assad"))
# print(obj.check_string_hash("sad"))
print(obj.check_string_ascii("nigawt"))