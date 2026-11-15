class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0] * n
        for num in range(n):
            prefix[num] = prefix[num - 1] + nums[num]
        return prefix 