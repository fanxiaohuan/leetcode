#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#


# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        # int()将二进制转换为十进制
        b = int(b,2)
        return bin(a+b)[2:]
        # bin()将十进制转换为二进制

# @lc code=end
if __name__ == "__main__":
    s=Solution()
    result = s.addBinary("11","1")
    print(result)
