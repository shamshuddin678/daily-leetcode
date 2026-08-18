class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # first window sum
        win_sum = sum(nums[ : k])
        max_sum = win_sum

        # slides the window
        for i in range(k,len(nums)):
            win_sum += nums[i] - nums[i-k]
            if(win_sum > max_sum):
                max_sum = win_sum
        return max_sum / float(k)