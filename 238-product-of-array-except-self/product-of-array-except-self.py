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

        #  Optimal solution for time complexity
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n

        # Build Prefix Array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build Suffix Array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Build Answer
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans   
        
        
        
        
        
        
        
        '''# optimal solution space complexity = O(1)
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

        return ans  '''