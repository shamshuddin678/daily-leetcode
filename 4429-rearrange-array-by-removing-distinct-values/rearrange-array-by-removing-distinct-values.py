from collections import Counter
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        ans = []

        while(freq):
            for i in sorted(freq):
                ans.append(i)
                freq[i] -= 1
                if(freq[i] == 0):
                    del freq[i]
        return ans