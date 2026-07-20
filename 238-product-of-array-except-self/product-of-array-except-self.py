class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        Brute force:
        ans = []
        n = len(nums)

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            ans.append(prod)
        return ans'''

        # optimal solution
        n = len(nums)
        ans = [1] * n

        # Prefix
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        # Suffix
        suffix = 1
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix

        return ans  