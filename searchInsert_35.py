# encoding:utf-8
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#
# @way 
# @from 
# @description enumrate() 字典遍历 数组遍历
# @result 
# @O 
# @time 2020-08-02 23:43:24
# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            if target < nums[0]:
                return 0
            elif target >nums[len(nums)-1]:
                return len(nums)
        for key,value in enumerate(nums):
            if target < value:
                return key
            elif target == value:
                return key
            # elif target > value:
            #     result = key
         
        
# @lc code=end
s=Solution()
print s.searchInsert([1,2,4,6],8)
