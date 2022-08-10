#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/10 9:47
from typing import List, Optional

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)