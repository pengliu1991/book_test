#!/usr/bin/env python
# -*- coding:utf-8 -*-

#---*kmp字符串匹配算法*----
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k==-1 or p[i]==p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def KMPmatching(t, p, pnext):
    """ KMP string mateching, the main function."""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j+1, i+1
        else:
            i = pnext[i]
    if i == m:
        return j-i
    return -1
p = "abab"
print gen_pnext(p)
# def matching(t, p):
#     print KMPmatching(t, p, gen_pnext(p))
# t = "abbabababbbbababaaaabababbbaaa"
# p = "aabab"
# matching(t, p)

