#!/usr/bin/env python
# -*- coding:utf-8 -*-

#---*完全背包问题*----
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def CompletePack(N, V, weight, value):
    """
    完全背包问题(每个物品可以取无限次)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :return: 返回最大的总价值
    """
    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, V+1):
            # 注意由于weight、value数组下标从0开始，第i个物品的容量为weight[i-1],价值为value[i-1]
            # V/weight[i-1]表示物品i最多可以取多少次
            f[i][j] = f[i - 1][j]  # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(j/weight[i-1]+1):
                if f[i][j] < f[i-1][j-k*weight[i-1]]+k*value[i-1]:
                    f[i][j] = f[i-1][j-k*weight[i-1]]+k*value[i-1]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            #  f[i][j] = max([f[i-1][j-k*weight[i-1]]+k*value[i-1] for k in range(j/weight[i-1]+1)])
    max_value = f[N][V]
    return max_value

if __name__ == '__main__':
    V = 10
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    N = len(weight)
    print CompletePack(N, V, weight, value)
