from collections import Counter
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter()
        freq[0] = 1
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            if(prefix - x in freq):
                ans += freq[prefix - k]
            freq[prefix] += 1
        return ans