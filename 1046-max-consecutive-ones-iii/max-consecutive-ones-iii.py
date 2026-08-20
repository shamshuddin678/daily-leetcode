class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        left = 0
        zero_count = 0
        ans = 0

        for right in range(len(nums)):
            # add right eleemnt
            if(nums[right] == 0):
                zero_count += 1
            
            #  if window becomes valid or not shrink left
            while(zero_count > k):
                if(nums[left] == 0):
                    zero_count -= 1
                left += 1
            # update ans
            ans = max(ans,right - left + 1)
        return ans