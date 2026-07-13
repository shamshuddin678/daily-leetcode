class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(list(set(nums)),reverse=True) # sort in descending order
        if(len(s) < 3):
            return max(s) 
        return s[2] # Returns the max of the 3rd element