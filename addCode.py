def twoSum(nums, target):
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
    print data
    return None
        



if __name__ == '__main__':
    # main()
    nums = [2, 7, 11, 15]
    target = 9
    date=twoSum(nums,target)
    print date
