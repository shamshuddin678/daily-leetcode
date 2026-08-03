class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(nums) != len(set(nums))
         
        # using set
        seen = set()

        for num in nums:
            if(num in seen):
                return True
            seen.add(num)
        return False