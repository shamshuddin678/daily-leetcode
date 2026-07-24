class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        total = 0
        diff = 0

        for c in t:
            total += ord(c) - ord('a')

        for c in s:
            diff += ord(c) - ord('a')

        return chr(total - diff + ord('a'))