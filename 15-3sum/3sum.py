class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        '''
        Method 1 : Brute Force Approach
        ans = []
        dup_re = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if tuple(triplet) not in dup_re:
                            dup_re.add(tuple(triplet))
                            ans.append(triplet)
        return ans  '''
        # Better solution
        ans = []
        dup = set()   # To avoid duplicate triplets
        n = len(nums)

        for i in range(n):
            hashset = set()

            for j in range(i + 1, n):

                k = -(nums[i] + nums[j])

                if k in hashset:
                    triplet = sorted([nums[i], nums[j], k])

                    if tuple(triplet) not in dup:
                        dup.add(tuple(triplet))
                        ans.append(triplet)

                hashset.add(nums[j])

        return ans
