class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        original = x
        rev = 0
        while(x > 0):
            lastdigit = x % 10
            rev = rev * 10 + lastdigit
            x = x // 10
        if(original == rev):
            return True
        else:
            return False