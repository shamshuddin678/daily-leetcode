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
        
        '''Better solution
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

        return ans'''
        
        # Two pointer approach
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = n - 1
            while(j < k):
                tot = nums[i] + nums[j] + nums[k] 
                if(tot < 0):
                    j += 1
                elif(tot > 0):
                    k -= 1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while(j < k and nums[j] == nums[j-1]): j+=1        
                    while(j < k and nums[k] == nums[k+1]): k-=1
        return ans                
