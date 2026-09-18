class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def ispalindrome(left,right):
            while(left < right):
                if(s[left] != s[right]):
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1
        while(left < right):
            if(s[left] != s[right]):
                # here skip either left or right
                return ispalindrome(left + 1,right) or ispalindrome(left,right - 1)
            left += 1
            right -= 1
        return True
            