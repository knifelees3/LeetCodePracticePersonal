"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_start=0
        len_str=len(s)
        len_max=1
        if len_str==0:
            len_max=0
        else:
            for l in range(len_str):
                index_end = l+1
                str_test=list(s[index_start:index_end])
                str_before=list(s[index_start:index_end-1])
                if len(str_before)>len_max:
                    len_max=len(str_before)
                print(s[index_end-1],str_test)
                if s[index_end-1] in str_before:
                    index_start=index_start+str_before.index(s[index_end-1])+1
                    str_tmp=s[index_start:index_end-1]
                    print(str_tmp)
                    if len(str_tmp)>len_max:
                        len_max=len(str_tmp)
                    print(len_max)
                elif len(str_test)>len_max:
                    len_max=len(str_test)
        return len_max
# %%
