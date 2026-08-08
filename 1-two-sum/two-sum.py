class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        ''' Brute force
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i] + nums[j] == target):
                    return i,j'''
        # Optimal Solution using the Hashmap
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in hashmap):
                return [hashmap[diff],i]
            hashmap[nums[i]] = i