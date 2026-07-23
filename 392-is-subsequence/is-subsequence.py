class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        max_index = 0
        for char in s:
            if char not in t[max_index:] or max_index == len(t):
                return False
            max_index += t[max_index:].index(char) + 1
        return True