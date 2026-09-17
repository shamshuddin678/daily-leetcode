class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        ans = 0

        for start in range(n):
            for end in range(start,n):
                length = end - start + 1
                
                if(length % 2 == 1):
                    for k in range(start,end + 1):
                        ans += arr[k]
        return ans