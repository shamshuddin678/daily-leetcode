class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while(left < right):
            mid = (left + right) // 2
            if(nums[mid] >= target):
                right = mid # target is left side move right
            else:
                left = mid + 1 # target is right side move left
        return left