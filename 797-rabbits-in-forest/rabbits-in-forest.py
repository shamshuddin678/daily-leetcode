from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        freq = Counter(answers)
        ans = 0

        for i,count in freq.items():
            group_size = i + 1
            groups = (count + group_size - 1) // group_size
            ans += groups * group_size
        return ans