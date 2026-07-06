class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        def ncr(n, r):
            result = 1
            for i in range(r):
                result = result * (n - i)
                result = result // (i + 1)
            return result

        ans = []

        for row in range(numRows):
            temp = []

            for col in range(row + 1):
                temp.append(ncr(row, col))

            ans.append(temp)

        return ans