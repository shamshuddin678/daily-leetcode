class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        monotone_incre = True
        monotone_decre = True

        for i in range(len(nums) - 1):
            # for the increase voilates
            if(nums[i] > nums[i + 1]):
                monotone_incre = False
            # for the decrease voilates
            if(nums[i] < nums[i + 1]):
                monotone_decre = False
        return monotone_incre or monotone_decre