#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/7 12:30
class Solution:

    def solve(self, nums, k):
        tar_remainder = (sum(nums)+k) % k
        if tar_remainder == 0:
            return 0
        n, presum = len(nums), 0

        res = n
        a_dict = {}
        for index, value in enumerate(nums):

            presum += value
            endindex = (presum+k) % k
            a_dict[endindex] = index
            preindex = (endindex - tar_remainder + k) % k
            if preindex in a_dict:
                res = min(res, index - a_dict[preindex])

        return res if res < n else -1





