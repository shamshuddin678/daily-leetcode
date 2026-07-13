class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)): # traverse the list
            if flowerbed[i] == 0:# check whether currnt plot is empty
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) # here check the right
                if left and right:
                    flowerbed[i] = 1 # can we plant
                    n -= 1
                    if n == 0: # if all flowers are planted
                        return True

        return n <= 0