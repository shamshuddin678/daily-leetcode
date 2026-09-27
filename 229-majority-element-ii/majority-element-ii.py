from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        res = []
        for num,count in freq.items():
            if(count > len(nums) // 3):
                res.append(num)
        return res