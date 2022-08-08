#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/8 23:08

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        if not head:
            return None

        num = 0
        temp_head = head
        while temp_head:
            num += 1
            temp_head = temp_head.next

        mid_index = num // 2

        for i in range(mid_index):
            head = head.next

        return head
