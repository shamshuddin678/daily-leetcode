class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadanes' with indices
        current_sum = nums[0]
        max_sumsofar = nums[0]

        start = 0
        best_start = 0
        best_end = 0

        for i in range(1,len(nums)):
            if(nums[i] > current_sum + nums[i]):
                current_sum = nums[i]
                start = i
            else:
                current_sum += nums[i]
            
            # for boundaries when we find the new max 
            if(current_sum > max_sumsofar):
                max_sumsofar = current_sum
                best_start = start
                best_end = i
        subarray = nums[best_start : best_end + 1]
        return max_sumsofar 