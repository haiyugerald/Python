#!/usr/bin/python
#-*- coding:utf-8 –*-

l=[1,2,10,30,33,99,101,200,301,402] #从小到大排列的数字列表
def search(num,l):
    print(l)
    if len(l) > 0:
        mid=len(l)//2
        if num > l[mid]: #在右边查找
            l=l[mid+1:]  #切右半边
        elif num < l[mid]: #在左边查找
            l=l[:mid]      #切左半边
        else:
            print('find it')
            return
        search(num,l)
    else:
        #如果值不存在，则列表切为空
        print('not exists')
        return
search(100,l)