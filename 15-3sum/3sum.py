class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = set()
        # better soln : Hashing
        for i in range(n):
            target = - nums[i]
            seen = set()
            for j in range(i + 1,n):
                b = nums[j]
                c = target - b
                if(c in seen):
                    triplet = tuple(sorted([nums[i],b,c]))
                    res.add(triplet)
                seen.add(b)
        return [list(x) for x in res]