<<<<<<< HEAD
#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#
# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,}
        # romanDouberDic={'IV':4,'IX':9,'XL':40,'XC':90,'CD':500,'CM':900}
        # keys=['I','V','X','L','C','D','M']
        # values=['1','5','10','50','100','500','1000']
        # romanStr=zip(keys,values)
        number=0
        for key in range(len(s)):
            if key<len(s)-1 and romanDic[s[key]]<romanDic[s[key+1]]:
            # value=romanDic[key]
            # num=int(value)
                number-=romanDic[s[key]]
            else:
                number+=romanDic[s[key]]

        return number



# @lc code=end
s=Solution()
s.romanToInt("IV")

=======
#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#
# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,}
        # romanDouberDic={'IV':4,'IX':9,'XL':40,'XC':90,'CD':500,'CM':900}
        # keys=['I','V','X','L','C','D','M']
        # values=['1','5','10','50','100','500','1000']
        # romanStr=zip(keys,values)
        number=0
        for key in range(len(s)):
            if key<len(s)-1 and romanDic[s[key]]<romanDic[s[key+1]]:
            # value=romanDic[key]
            # num=int(value)
                number-=romanDic[s[key]]
            else:
                number+=romanDic[s[key]]

        return number



# @lc code=end
s=Solution()
s.romanToInt("IV")

>>>>>>> 91df478... 公司代码合并
