"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

class Permutation:
    def check_permutation_conventional(self, child, parent):
        in_child = {}

        if len(child) != len(parent):
            return False

        for item in child:
            in_child[item] = False
            if item in parent:
                in_child[item] = True

        if False in in_child.values():
            return False
        return True


perm_obj = Permutation()


print(perm_obj.check_permutation_conventional("asdsad", "asdasd"))
