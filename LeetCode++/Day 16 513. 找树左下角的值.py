#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/7/30 7:56

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:

    def __init__(self):
        self.max_depth = 0
        self.depth = 0
        self.res = TreeNode()

    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth
            self.res = root

        self.traverse(root.left)
        self.traverse(root.right)

        self.depth -= 1

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res.val



