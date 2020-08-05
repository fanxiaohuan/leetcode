#
# @lc app=leetcode.cn id=7 lang=python
#
# 
#

# @lc code=start
class Solution(object):
    # def reverseFor(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     num = 0
    #     if x == 0:
    #         return 0
    #     if x < 0:
    #         x = -x
    #         while x != 0:
    #             num = num*10 + x%10
    #             x = x/10
    #         num = -num
    #     else:
    #         while x != 0:
    #             num = num*10 + x%10
    #             x = x/10           
    #     if num>pow(2,31)-1 or num < pow(-2,31):
    #         return 0
    #     return num
    def reverse(self, x):
        if x<0:
            x=-x
            f='-'
        else:
            f=''
        xstr=str(x)
        data=xstr[::-1]
        string=f+data
        
        if int(string)>pow(2,31)-1 or int(string) < pow(-2,31):
            return 0
        return int(string)
        

s = Solution()
t=-2147483649
value=s.reverse(t)
print(value)
      
# @lc code=end

