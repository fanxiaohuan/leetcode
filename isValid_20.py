#utf-8
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# @way 
# @from 
# @description 栈  append() 添加 pop()弹出
# @result ac
# @O N
# @time 2020-08-04 22:13:13
# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={"(":")","[":"]","{":"}","?":"?"}
        stack=["?"]
        for key in s:
            if key in dic:
                stack.append(key)
            elif dic[stack.pop()]!=key:
                return False
        return len(stack)==1
# @lc code=end
s=Solution()
print s.isValid("()}]")

