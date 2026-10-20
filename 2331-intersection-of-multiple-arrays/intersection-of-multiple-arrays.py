class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for num in nums[0]:
            found_everywhere = True
            for arr in nums[1:]:
                if(num not in arr):
                    found_everywhere = False
                    break
            if(found_everywhere and num not in res):
                res.append(num)
        res.sort()
        return res