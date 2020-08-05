#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
# @way 
# @from 
# @description 
# @result 
# @O 
# @time 2020-08-02 20:17:53
import copy
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        key = 0
        for i in range(len(nums)):
            if nums[key] != nums[i]:
                key+=1
                nums[key]=nums[i]
        return key+1
# @lc code=end
numList=[1,1,2,3,3,4]
s=Solution()
s.removeDuplicates(numList)