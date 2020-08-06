# encoding:utf-8
#
# @lc app=leetcode.cn id=1480 lang=python
#
# [1480] 一维数组的动态和
#
# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runingSmList=nums
        for i in range(1,len(nums)):
            runingSumList[i]=nums[i]+runingSumList[i-1] 
        
        return runingSumList


# @lc code=end

if __name__ == "__main__":
    s=Solution()
    result=s.runningSum([1,2,3,5])
    print(result)


