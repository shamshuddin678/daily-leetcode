class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            digit = nums[i]

            total = 0
            while(digit > 0):
                total += digit % 10
                digit //= 10
            if(total == i):
                return i
        return -1