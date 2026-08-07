class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmax = maxsofar = nums[0]
        #  Kaden's array traversal
        for i in range(1,len(nums)):
            currmax = max(nums[i],currmax + nums[i])
            maxsofar = max(maxsofar,currmax)
        return maxsofar