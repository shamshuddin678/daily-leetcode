class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''Here the one line 
        return len(nums) != len(set(nums))'''
        # using the set 
        seen = set()

        for num in nums:
            if(num in seen):
                return True
            seen.add(num)
        return False