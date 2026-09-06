class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if(num < 0):
                max_prod , min_prod = min_prod , max_prod

            max_prod = max(num,max_prod * num)
            min_prod = min(num,min_prod * num)
            ans = max(ans,max_prod)
        return ans 