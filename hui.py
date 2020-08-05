<<<<<<< HEAD
#
# @lc app=leetcode.cn id=9 lang=python
# @lc code=start
class Solution(object):
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

=======
#
# @lc app=leetcode.cn id=9 lang=python
# @lc code=start
class Solution(object):
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

>>>>>>> 91df478... 公司代码合并
# @lc code=end