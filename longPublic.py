<<<<<<< HEAD
# encoding:utf-8
# @lc app=leetcode.cn id=14 lang=python
# [14] 最长公共前缀
#
# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        maxStr = max(strs)
        minStr =  min(strs)
        for i,k in enumerate(minStr):
            # 下标和字符串值组合成字典 enumerate()
            if k != maxStr[i]:
                result=maxStr[:i]
                return result
            
        return minStr
        
# @lc code=end
s=Solution()
key=s.longestCommonPrefix(["agh","cdd","ee"])
print key

=======
# encoding:utf-8
# @lc app=leetcode.cn id=14 lang=python
# [14] 最长公共前缀
#
# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        maxStr = max(strs)
        minStr =  min(strs)
        for i,k in enumerate(minStr):
            # 下标和字符串值组合成字典 enumerate()
            if k != maxStr[i]:
                result=maxStr[:i]
                return result
            
        return minStr
        
# @lc code=end
s=Solution()
key=s.longestCommonPrefix(["agh","cdd","ee"])
print key

>>>>>>> 91df478... 公司代码合并
