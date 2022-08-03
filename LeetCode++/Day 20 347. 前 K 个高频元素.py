#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/3 10:41
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a_list = []
        a_dict = {}
        for i in nums:
            if i not in a_dict:
                a_dict[i] = 1
            else:
                a_dict[i] += 1

        b_dict = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)[:k]
        for i in b_dict:
            a_list.append(i[0])
        return a_list




