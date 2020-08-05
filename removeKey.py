#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#
# @way 倒序遍历数组
# @from https://www.jianshu.com/p/e20c78153299
# @description 遍历数组删除指定值 
# @result 
# @O n
# @time 2020-08-02 22:15:45
# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tempnums = nums[::-1]
        for i in range(len(nums)-1,0,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
# @lc code=end
s=Solution()
s.removeElement([1,2,3,3,4],3)

