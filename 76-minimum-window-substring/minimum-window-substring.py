from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        window = Counter()

        left = 0
        have = 0
        required = len(need)
        minlen = float('inf')
        start = 0

        for right in range(len(s)):
            window[s[right]] += 1
            if(s[right] in need and window[s[right]] == need[s[right]]):
                have += 1
            while(have == required):
                if(right - left + 1 < minlen):
                    minlen = right - left + 1
                    start = left
                if(s[left] in need and window[s[left]] == need[s[left]]):
                    have -= 1
                window[s[left]] -= 1
                left += 1
        if minlen == float('inf'):
            return ""

        return s[start:start + minlen]