class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fre = {}
        left = 0
        maxlen = 0
        for right in range(len(fruits)):
            fre[fruits[right]] = fre.get(fruits[right], 0) + 1
            while len(fre) > 2:
                fre[fruits[left]] -= 1

                if fre[fruits[left]] == 0:
                    del fre[fruits[left]]
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen