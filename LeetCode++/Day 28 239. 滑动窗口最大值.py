#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/14 22:22
from typing import List
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a_list = []
        mydeque = collections.deque()
        len_nums = len(nums)

        for i in range(len_nums):

            while mydeque and nums[mydeque[-1]] < nums[i]: mydeque.pop()
            while mydeque and mydeque[0] <= i - k: mydeque.popleft()
            mydeque.append(i)
            if i >= k - 1:
                a_list.append(nums[mydeque[0]])

        return a_list

t = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
a = t.maxSlidingWindow(nums, k)
print(a)