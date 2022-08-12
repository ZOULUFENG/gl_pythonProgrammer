#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/12 16:23
from typing import List, Optional

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_dict = {}
        a_list = []
        if n == 1:
            return n
        if n > 1 and len(trust) == 0:
            return -1
        for i in trust:
            a_dict[i[1]] = a_dict.get(i[1], 0) + 1
            a_list.append(i[0])

        for i in a_dict.keys():
            if a_dict[i] == n - 1 and i not in a_list:
                return i
        return -1


# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 4
trust = [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]
t = Solution()
a = t.findJudge(4, trust)
print(a)