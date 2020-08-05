# encoding:utf-8
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#
# @way 
# @from 
# @description split() 异常情况考虑 倒序遍历
# @result Ac
# @O n
# @time 2020-08-02 23:44:28

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 字符串为空 返回0
        if len(s)==0:
            return 0
        else:
            data=s.split(' ')
            key=len(data)
            # 最后一个非空
            if data[-1] != '':
                # lastWord=
                return len(data[-1])
            else:
                # 最后有多个空格
                for i in data[::-1]:
                  if i !='':
                      return len(i)
                reslut=data[len(data)-2]
                return len(reslut)
    
# @lc code=end
s=Solution()
print s.lengthOfLastWord("hello a    ")

