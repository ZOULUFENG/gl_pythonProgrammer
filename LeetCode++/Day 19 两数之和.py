#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/2 9:31
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a_dict = {}
        for index, value in enumerate(nums):
            m = target - value
            if m in a_dict:
                return [a_dict[m], index]
            else:
                a_dict[value] = index