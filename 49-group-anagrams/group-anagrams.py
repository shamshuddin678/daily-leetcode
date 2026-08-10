class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)

        for s in strs:
            hash = str(sorted(list(s)))
            hashmap[hash].append(s)
        return hashmap.values()