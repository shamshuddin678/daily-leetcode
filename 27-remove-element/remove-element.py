class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        approach 1:
        i = 0
        for j in range(len(nums)):
            if(nums[j] != val):
                nums[i] = nums[j]
                i += 1
        return i '''
        while val in nums:
            nums.remove(val)       