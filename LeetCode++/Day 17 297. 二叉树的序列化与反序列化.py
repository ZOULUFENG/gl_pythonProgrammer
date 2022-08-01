#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/7/31 10:00
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.a_str = ""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.traverse(root)
        return self.a_str

    def traverse(self, root):
        if not root:
            self.a_str += "#,"
            return None
        self.a_str += str(root.val)
        self.a_str += ','
        self.serialize(root.left)
        self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        a_list = data.split(',')
        print(a_list)
        return self.traverse_de(a_list)

    def traverse_de(self, a_list):

        if not a_list:
            return None

        num = a_list.pop(0)
        if num == '#':
            return None

        if num == '-':
            tnum = a_list.pop(0)
            root = TreeNode(-int(tnum))
        else:
            root = TreeNode(int(num))

        root.left = self.traverse_de(a_list)
        root.right = self.traverse_de(a_list)

        return root