class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd_chars = set()
        length = 0

        for c in s:
            if(c in odd_chars):
                odd_chars.remove(c)
                length += 2
            else:
                odd_chars.add(c)
        if(odd_chars):
            length += 1
        return length