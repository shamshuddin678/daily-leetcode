class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Here this is method 1 -> return nums.sort()
        # Here method 2 -> Dutch National Flag Algorithm
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        '''
        -> high = 0 index based = high[2] = 1
        -> 2,0,1 . low,mid = 2 and high = 1 swap
        ->1. 1,0,2 . low,mid = 1, and high -= 1 then it is high = 0 .
        ->2. after swap => 0,1,2 
        '''     