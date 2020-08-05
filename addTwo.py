<<<<<<< HEAD
#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 定义空字典
        data = {}
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
        # 同时列出数据和数据下标，一般用在 for 循环当中
        for i, num in enumerate(nums):
            result = target - num
            # 判断值是否在字典中
            if result in data:
                return [data[result], i]
            data[num] = i
        
            # 将当前数组值与数据下标写入字典
        # print data
        return None
# python 定义class类函数
# s = Solution()
# s.twoSum([2,5,7,4],9)
# print s
                    


        
# @lc code=end

=======
#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 定义空字典
        data = {}
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
        # 同时列出数据和数据下标，一般用在 for 循环当中
        for i, num in enumerate(nums):
            result = target - num
            # 判断值是否在字典中
            if result in data:
                return [data[result], i]
            data[num] = i
        
            # 将当前数组值与数据下标写入字典
        # print data
        return None
# python 定义class类函数
# s = Solution()
# s.twoSum([2,5,7,4],9)
# print s
                    


        
# @lc code=end

>>>>>>> 91df478... 公司代码合并
