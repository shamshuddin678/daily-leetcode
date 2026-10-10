from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums1)
        res = []
        for num in nums2:
            if(freq[num] > 0):
                res.append(num)
                freq[num] -= 1
        return res