class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method 1: return len(s.split()[-1])
        
        # Method 2:
        words = s.strip().split()

        if(not words):
            return 0
        return len(words[-1])    