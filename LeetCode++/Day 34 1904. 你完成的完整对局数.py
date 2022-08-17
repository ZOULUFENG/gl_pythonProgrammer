#!/usr/bin/env python39
# -*- coding:utf-8 -*-
# author:GL
# @time: 2022/8/17 11:20
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        a_num = 0
        b_num = 0
        a_num = int(loginTime[:2]) * 4 + int(loginTime[3:]) // 15 + bool(int(loginTime[3:]) % 15)
        b_num = int(logoutTime[:2]) * 4 + int(logoutTime[3:]) // 15
        if int(loginTime[:2]) * 60 + int(loginTime[3:]) > int(logoutTime[:2]) * 60 + int(logoutTime[3:]):
            b_num += 24 * 4
        if b_num - a_num == -1:
            return 0
        return b_num - a_num

# 使用map实现批量的类型转换
# 规范化输入,可以降低后续的处理难度.比如时间的信息.
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        sh, sm = map(int, startTime.split(":"))
        eh, em = map(int, finishTime.split(":"))
        d = 0
        if sh * 60 + sm > eh * 60 + em: d += 1
        if 0 < sm <= 15:
            sm = 15
        elif 15 < sm <= 30:
            sm = 30
        elif 30 < sm <= 45:
            sm = 45
        elif 45 < sm <= 60:
            sm = 0
            sh += 1
        if 0 <= em < 15:
            em = 0
        elif 15 <= em < 30:
            em = 15
        elif 30 <= em < 45:
            em = 30
        elif 45 <= em < 60:
            em = 45
        st = sh * 60 + sm
        et = eh * 60 + em
        if d == 1: et += 24 * 60
        return max(0, (et - st)) // 15
