#!/usr/bin/env python
# -*- coding:utf-8 -*-

#---*排序问题*----
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import random

#插入排序
def insert_sort(lst):
    count = len(lst)
    for i in range(1, count):
        key = lst[i]
        j = i - 1
        while j >= 0:
            if lst[j] > key:
                lst[j+1] = lst[j]
                lst[j] = key
            j -= 1
    return lst

#冒泡排序
def bubble_sort(lst):
    count = len(lst)
    for i in range(0, count):
        found = False
        for j in range(i+1, count):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                found = True
            if not found:
                break
    return lst

#快速排序
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] == lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1)
    quick_sort(lists, left+1, high)
    return lists

def get_andomNumber(num):
    lists=[]
    i=0
    while i<num:
        lists.append(random.randint(0,100))
        i+=1
    return lists

a = get_andomNumber(10)
print("排序之前：%s" %a)

b = insert_sort(a)
print("排序之后：%s" %b)

c = bubble_sort(a)
print("排序之后：%s" %c)
