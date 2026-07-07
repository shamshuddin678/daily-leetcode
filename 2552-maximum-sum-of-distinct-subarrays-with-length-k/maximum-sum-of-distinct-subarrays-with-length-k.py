class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        freq = {}
        window_sum = 0
        ans = 0
        left = 0

        for right in range(len(nums)):

            # Add current element
            window_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Window size becomes greater than k
            if right - left + 1 > k:

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                window_sum -= nums[left]
                left += 1

            # Check valid window
            if right - left + 1 == k:

                if len(freq) == k:
                    ans = max(ans, window_sum)

        return ans