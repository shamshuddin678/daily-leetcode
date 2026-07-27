class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # compute the sum of thw first window
        win_sum = sum(nums[:k])
        max_sum = win_sum

        # Slide the window : add the new element (left) and remove the old element
        for i in range(k,len(nums)):
            win_sum += nums[i] - nums[i-k]
            if(win_sum > max_sum):
                max_sum = win_sum
        return max_sum/ float(k)