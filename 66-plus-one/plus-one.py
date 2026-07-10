class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = int("".join(map(str,digits))) # heer convert into number
        a += 1
        return list(map(int,str(a)))