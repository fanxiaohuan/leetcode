#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] !=9 :
                digits[i] = digits[i]+1
                # print(digits)
                return digits
            else:
                digits[i] = 0
                # digits[i+1]+=digits[i+1]
                if digits[0] == 0:
                    digits.insert(0,1)
                    return digits

# @lc code=end
if __name__ == "__main__":
    s=Solution()
    valuelist=s.plusOne([1,9,9])
    print(valuelist)
