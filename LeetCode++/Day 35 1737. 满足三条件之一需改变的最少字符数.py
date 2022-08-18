#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/18 10:10
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a_list = []
        # 第一种情况:改短的字符串
        len_a = len(a)
        len_b = len(b)
        first_solution = len_b if len_b < len_a else len_a
        a_list.append(first_solution)

        # 第二种情况:改成同一字符
        a_count = []
        b_count = []
        a_count_fix = 0
        b_count_fix = 0
        for i in a:
            a_count.append(a.count(i))
        a_count_max = max(a_count)
        a_count_fix = len_a - a_count_max
        for i in b:
            b_count.append(b.count(i))
        b_count_max = max(b_count)
        b_count_fix = len_b - b_count_max
        second_solution = a_count_fix + b_count_fix
        a_list.append(second_solution)

        # 第三种情况:看看有多少个字母是a小于b 或者是b小于a
        a_big_b_number = 0
        b_big_a_number = 0
        a_small_char = min(a)
        b_small_char = min(b)
        for i in a:
            if i >= b_small_char:
                a_big_b_number += 1
        for i in b:
            if i >= a_small_char:
                b_big_a_number += 1
        third_solution = a_big_b_number if a_big_b_number < b_big_a_number else b_big_a_number
        a_list.append(third_solution)

        # 第四种情况:看看有多少个字母是a大于b 或者是b大于a
        a_small_b_number = 0
        b_small_a_number = 0
        a_big_char = max(a)
        b_big_char = max(b)
        for i in a:
            if i <= b_big_char:
                a_small_b_number += 1
        for i in b:
            if i <= a_big_char:
                b_small_a_number += 1
        forth_solution = a_small_b_number if a_small_b_number < b_small_a_number else b_small_a_number
        a_list.append(forth_solution)

        # 第五种情况: 考虑相等字符的因素
        a_equal_b_number = 0
        b_equal_a_number = 0
        a_equal_b_list = []
        b_equal_a_list = []
        for i in a:
            if i in b:
                a_equal_b_number += 1
                a_equal_b_list.append(i)
        for i in b:
            if i in a:
                b_equal_a_number += 1
                b_equal_a_list.append(i)

        return min(a_list)




a = "ace"
b = "abe"
# a = "acac"
# b = "bd"
t = Solution()
f = t.minCharacters(a, b)
print(f)
