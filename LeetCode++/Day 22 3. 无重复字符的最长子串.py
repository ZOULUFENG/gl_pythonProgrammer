#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/5 22:57
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        len_s  = len(s)
        left, right = 0, 0
        windows = {}
        while right < len_s:
            char = s[right]
            right += 1
            if char in windows.keys():
                windows[char] += 1
            else:
                windows[char] = 1

            while windows[char] > 1:
                w_char = s[left]
                left += 1
                windows[w_char] -= 1

            res = max(res, right - left)
        return res

t = Solution()
s = "abcabcbb"

print(t.lengthOfLongestSubstring(s))


