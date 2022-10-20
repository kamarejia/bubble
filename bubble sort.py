#!/usr/bin/env python
# coding: utf-8




import random
n=int(input("データはいくつにしますか？"))
a=[random.randint(1,100) for i in range(n)]
print(a) 
def ascending_bubble(a):
    
    length=len(a)
    for i in range(1,length):
        for j in range(0,length-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                print(a)
    return a
   
def descending_bubble(a):
    
    length=len(a)
    for i in range(1,length):
        for j in range(0,length-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                print(a)
    return a
   
    
    
  
sequential=int(input("昇順なら1,降順なら0と入力してください。"))
if sequential==1:
    print(f"昇順：{ascending_bubble(a)}")
    
else:
    print(f"降順:{descending_bubble(a)}")








