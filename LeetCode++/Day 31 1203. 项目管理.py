#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/14 22:57
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        b_list = []
        # 设立m个小组
        a_list = {}
        # 把下标处理一下
        t_group = []
        for i in group:
            if i == -1:
                i = m
            t_group.append(i)

        # 把项目分组
        for index, value in enumerate(t_group):
            if value not in a_list:
                a_list[value] = []
            a_list[value].append(index)

        # 对小组的顺序进行排序
        # [0, 2]
        c_list = []
        for index, value in enumerate(beforeItems):
            if value:
                for i in value:
                    if i not in a_list[t_group[index]]:
                        c_list.append(t_group[i])
                        c_list.append(t_group[index])
        len_c_list = len(c_list)
        for i in c_list:
            left = c_list.index(i)
            right = 0
            for j in range(len_c_list):
                if c_list[len_c_list-1-j] == i:
                    right = len_c_list-1-j
                    break

            if sum(c_list[left:right+1]) != i * (right+1-left):
                return []

        for i in range(m+1):
            if i not in c_list:
                c_list.append(i)

        for iii in c_list:
            for jjj in a_list[iii]:
                for zzz in beforeItems[jjj]:
                    if zzz not in b_list:
                        b_list.append(zzz)
                # if beforeItems[jjj]:
                #     for zzz in
                #     if beforeItems[jjj] in b_list
                #     b_list.extend(beforeItems[jjj])
                if jjj not in b_list:
                    b_list.append(jjj)
        return b_list



n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]


t = Solution()
a = t.sortItems(n, m, group, beforeItems)
print(a)




