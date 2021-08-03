"""
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# %%
def longestPalindrome(s: str) -> str:
    len_max=0
    s_max=s[0:1]
    len_s=len(s)
    # 奇数的部分
    for l in range(len_s):
        index_left=l
        index_right=l
        while index_left-1>=0 and index_right+1<=len_s-1:
            #print(index_left)
            index_left=index_left-1
            index_right=index_right+1
            if s[index_left]==s[index_right]:
                if len_max<index_right-index_left+1:
                    s_max=s[index_left:index_right+1]
                    len_max=index_right-index_left+1
            else:
                index_left=-3
    # 偶数的部分
    for l in range(len_s):
        index_left=l
        index_right=l+1
        while index_left>=0 and index_right<=len_s-1:
            #print(index_left)
            if s[index_left]==s[index_right]:
                if len_max<index_right-index_left+1:
                    len_max=index_right-index_left+1
                    s_max=s[index_left:index_right+1]
                index_left=index_left-1
                index_right=index_right+1
            else:
                index_left=-3
    return s_max

print(longestPalindrome('aacabdkacaa'))