class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_water = 0
        left = 0
        right = len(height) - 1
        # two pointer -> inward traversal approach
        while(left < right):
            water = min(height[left],height[right]) * (right - left)
            max_water = max(max_water,water)

            # moves pointers -> inward
            if(height[left] < height[right]):
                left += 1
            elif(height[left] > height[right]):
                right -= 1
            else:
                # if 2 heighta are equal
                left += 1
                right -= 1
        return max_water