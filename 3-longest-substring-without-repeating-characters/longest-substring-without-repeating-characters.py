from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = Counter()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1

            while(hashmap[s[right]] > 1):
                hashmap[s[left]] -= 1
                left += 1
            maxlen = max(maxlen,right - left + 1)
        return maxlen