#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#
# import cmath
# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # num = cmath.sqrt(x)
        num = x**0.5
        result=int(num)
        return result

# @lc code=end
if __name__ == "__main__":
    s=Solution()
    key=s.mySqrt(8)
    print(key)
