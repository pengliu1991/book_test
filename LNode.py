#!/usr/bin/env python
# -*- coding:utf-8 -*-
#---*节点类模块*----

class LNode :
    def __init__(self, elm, nxt=None):
        self.elem = elm
        self.next = nxt

if __name__ == '__main__':
    llist1 = LNode(1, None)
    pnode = llist1

    for i in range(2, 11):
        pnode.next = LNode(i, None)
        pnode = pnode.next

    pnode = llist1
    while pnode != None:
        print(pnode.elem)
        pnode = pnode.next