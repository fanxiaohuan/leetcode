#
# @lc app=leetcode.cn id=9 lang=python
# @lc code=start
class Solution(object):
    # @way 
    # @from 
    # @description 
    # @result 
    # O 
    # @time 2020-08-01 18:33:27
    def isPalindrome_flip(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xPalindrome = 0
        xCopy = x
        if x == 0:
            return True                                                                                                         
        if x < 0:
            return False

        while x!=0:
            xPalindrome = xPalindrome * 10 + x % 10             
            x = x / 10

        if xPalindrome == xCopy:
            return True
        else:
            return False

    # @way 
    # @from 
    # @description 
    # @result 
    # @O 
    # @time 2020-08-01 18:33:36
    def isPalindrome(self, x):
        xString = str(x)
        start = 0
        end = len(xString)-1
        while start <= len(xString)/2:
            if xString[start]!= xString[end]:
                return False
            start = start + 1
            end = end - 1
        return True

# @lc code=end