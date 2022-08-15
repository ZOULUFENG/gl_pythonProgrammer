#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/15 14:17
# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         a_dict = {}
#         for i in moves:
#             a_dict[i] = a_dict.get(i, 0) + 1
#
#         for i in a_dict.keys():
#             if i == 'L':
#                 if 'R' not in a_dict:
#                     return False
#                 else:
#                     if a_dict['R'] != a_dict['L']:
#                         return False
#             if i == 'R':
#                 if 'L' not in a_dict:
#                     return False
#                 else:
#                     if a_dict['R'] != a_dict['L']:
#                         return False
#             if i == 'U':
#                 if 'D' not in a_dict:
#                     return False
#                 else:
#                     if a_dict['U'] != a_dict['D']:
#                         return False
#             if i == 'D':
#                 if 'U' not in a_dict:
#                     return False
#                 else:
#                     if a_dict['U'] != a_dict['D']:
#                         return False
#
#         return True

# 写一个解法妙的
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for i in moves:
            if i == 'L': x -= 1
            if i == 'R': x += 1
            if i == 'U': y += 1
            if i == 'D': y -= 1

        return x == 0 and y == 0
