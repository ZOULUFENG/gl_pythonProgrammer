#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/9 13:41

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法一：使用遍历递归的方法
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return head

        fast, slow, end = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            end = slow
            slow = slow.next

        end.next = None

        temp_head = TreeNode(slow.val)
        if fast == slow:
            return temp_head

        temp_head.left = self.sortedListToBST(head)
        temp_head.right = self.sortedListToBST(slow.next)
        return temp_head





