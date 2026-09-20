class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s =  str(num)
        left = 0
        count = 0

        for right in range(len(s)):
            if(right - left + 1 == k):
                val = int(s[left : right + 1])
                if(val != 0 and num % val == 0):
                    count += 1
                left += 1
        return count