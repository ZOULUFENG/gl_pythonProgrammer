#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/4 10:00
from collections import defaultdict
from typing import List


class Solution:
    def calc_distance(self, list1, list2):
        return (list1[0] - list2[0]) ** 2 + (list1[1] - list2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        ans = 0
        for list1 in points:
            cnt = defaultdict(int)

            for list2 in points:
                dis = self.calc_distance(list1, list2)
                cnt[dis] += 1

            for i in cnt.values():
                ans += i * (i - 1)

        return ans


