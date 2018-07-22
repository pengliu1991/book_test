#!/usr/bin/env python
# -*- conding:utf-8 -*-

def st(N, K):
    N = str(N)
    n = len(N)
    m = len(K)
    c = 0
    i = 0
    flag = 1
    while i < n:
        com = N[i]
        if flag ==1:
            c_com, flag = compare(int(com), K)
            print c_com ,flag
            c = c + 10 ** (n - i -1) * int(c_com)
        elif flag == 0:
            c_com = K[m-1]
            c = c + 10 ** (n - i -1) * int(c_com)
        i = i+1
    return c


def compare(a, K):
    j = 0
    #print K
    n = len(K)
    for b in K:
        if a > b:
            j += 1
            if j == n:
                flag = 1
                return b, flag
                break
        elif a == b:
            flag = 1
            return a, flag
            break
        elif a < b:
            flag = 0
            return K[j-1], flag


if __name__ == "__main__":
    a = 1299
    k = [3, 8, 1]
    k.sort()
    bb = st(a, k)
    print bb