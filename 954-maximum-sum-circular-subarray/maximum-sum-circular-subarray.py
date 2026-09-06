class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)

        curr_max = nums[0]
        max_sum = nums[0]
        
        curr_min = nums[0]
        min_sum = nums[0]

        for num in nums[1:]:
            curr_max = max(num,curr_max + num)
            max_sum = max(max_sum,curr_max)

            curr_min = min(num,curr_min + num)
            min_sum = min(min_sum,curr_min)

        if(max_sum < 0):
            return max_sum
        circular = total - min_sum
        return max(max_sum,circular)