class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        total = 0
        diff = 0

        for c in t:
            total += ord(c) - ord('a')

        for c in s:
            diff += ord(c) - ord('a')

        return chr(total - diff + ord('a'))'''
        fre = {}
        for ch in t:
            fre[ch] = fre.get(ch, 0) + 1
        for ch in s:
            fre[ch] -= 1
        for ch, c in fre.items():
            if c > 0:
                return ch