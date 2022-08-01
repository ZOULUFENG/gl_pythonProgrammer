#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/7/29 11:16

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.num = 0
        if not root:
            return self.root
        def dfs(num, root):
            num  = num * 10 + root.val
            if not root.right and not root.left:
                self.num += num

            elif root.left:
                dfs(num, root.left)
            elif root.right:
                dfs(num, root.right)

        return self.num

