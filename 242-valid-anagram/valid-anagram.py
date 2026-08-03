from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        counter = Counter(s)

        for let in t:
            if(let not in counter or (counter[let] == 0)):
                return False
            counter[let] -= 1
        return True