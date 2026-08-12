from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)
        occurrences = count.values()

        return len(occurrences) == len(set(occurrences))