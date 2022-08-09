#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/9 10:08
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        temp_len_nums = len_nums
        if len_nums < 2:
            return len_nums
        first, last = 1, 0
        while first < temp_len_nums:
            if nums[first] == nums[last]:
                del nums[first]
                temp_len_nums -= 1
            else:
                first += 1
                last += 1

        return temp_len_nums
