#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/6 23:09
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        t_words = "".join(words)
        a_list = []
        len_words = len(words)
        len_words_let = len(words[0])
        s_len = len(s)
        words_dict = {}
        win_dict = {}
        if len_words == 0:
            return None

        # 获取words的字母频数
        for char in t_words:
            words_dict[char] = words_dict.get(char, 0) + 1

        left, right = 0, len(t_words)
        while right <= s_len:
            win_dict = {}
            temp_list = s[left:right]

            for index, char in enumerate(temp_list):
                win_dict[char] = win_dict.get(char, 0) + 1
                if char not in words_dict:
                    left += (index+1)
                    right += (index+1)
                    break
                elif win_dict[char] > words_dict[char]:
                    left += 1
                    right += 1
                    break
            else:
                for char in win_dict.keys():
                    if win_dict[char] < words_dict[char]:
                        left += 1
                        right += 1
                        break
                else:
                    b_list = []
                    for i in range(len_words):
                        b_list.append(temp_list[len_words_let*i:len_words_let*(i+1)])
                    for i in words:
                        if i not in b_list:
                            left += 1
                            right += 1
                            break
                        else:
                            b_list.remove(i)

                    else:

                        a_list.append(left)
                        left += 1
                        right += 1
        return a_list



# s = "wordgoodgoodgoodbestword"
# words = ["word", "good", "best", "good"]

s = "abababab"
words = ["ab","ab","ab"]
t = Solution()
a = t.findSubstring(s, words)
print(a)





