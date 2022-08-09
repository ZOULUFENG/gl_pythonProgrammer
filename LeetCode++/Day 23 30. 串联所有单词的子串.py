#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/6 23:09
from typing import List


class Solution:
    def findSubstring(self, s: str, twords: List[str]) -> List[int]:
        words = "".join(twords)
        flag = True
        a_list = []
        len_words = len(words)
        len_words_let = len(words[0])
        s_len = len(s)
        words_dict = {}
        win_dict = {}
        if len_words == 0:
            return None
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        left, right = 0, 0
        while right < s_len:

            char = s[right]
            win_dict[char] = win_dict.get(char, 0) + 1
            right += 1

            if char not in words_dict.keys() or win_dict[char] > words_dict[char]:
                left += 1

            for i in words_dict.keys():
                if win_dict[i] == words_dict[i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                a_list.append(left)

        return a_list


