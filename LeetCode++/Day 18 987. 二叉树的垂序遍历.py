#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/1 8:53
# Definition for a binary tree node.


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.a_list = []
        self.b_list = []
        self.c_list = []

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.traverse(root, 0, 0)
        return self.devide_grope(self.a_list)

        # print(self.b_list)

    def traverse(self, root, row, col):
        if not root:
            return None
        self.a_list.append([row, col, root.val])
        self.traverse(root.left, row + 1, col - 1)
        self.traverse(root.right, row + 1, col + 1)

    def devide_grope(self, data):
        self.b_list = sorted(data, key=lambda x: (x[1], x[0], x[2]))
        b_list = []
        c_list = []

        for i in self.b_list:
            if i[1] not in c_list:
                c_list.append(i[1])
                b_list.append('#')

            b_list.append(i[2])

        row = b_list.count('#')
        a_list = [[] for _ in range(row)]
        print(b_list)

        num = -1
        for i in b_list:
            if i == '#':
                num += 1
            else:
                a_list[num].append(i)
        return a_list



