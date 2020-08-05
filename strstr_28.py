#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()

# @lc code=start

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            length=len(needle)-1
            for i in range(len(haystack)):
                string = haystack[i:i+len(needle)]
                if needle == string:
                    return i


# @lc code=end


if __name__ == "__main__":
    s=Solution()
    value=s.strStr("mississippi","sipp")
    print(value)
