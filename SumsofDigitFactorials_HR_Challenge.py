# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:20:54 2020

@author: pratiksha.garode
"""
import math

def f(n):
    x = 0
    while(n >= 1):
        rem = n%10
        fact = math.factorial(rem)
        x = x + fact
        n = n//10
    return x

def sf(n):
    num = f(n)
    arr = []
    while(num >= 1):
        rem = num%10
        arr.append(rem)
        num = num//10
        sumArr = sum(arr)
    return sumArr

def g(i):
    count = 1
    while(count<pow(10,18)):
        print(count)
        if(sf(count) == i):
            return count
        count += 1
     #-----------------check-----------------#

def sg(i):
    num = g(i)
    arr = []
    while(num >= 1):
        rem = num%10
        arr.append(rem)
        num = num//10
        sumArr = sum(arr)
    return sumArr


def calM(n,m):
    j = 1
    x = 0
    while(j<=n):
        x = x + sg(j)
        j += 1
    return x%m

calM(50, 1000000)



from sys import stdin, stdout 

q = int(stdin.readline())
while(q!=0):
    arr = [int(x) for x in stdin.readline().split()] 
    
    n = arr[0]
    m = arr[1]
    print(calM(n,m))
    q -= 1



from sys import stdin, stdout 

q = 2
while(q!=0):
   
    print(calM(3, 1000000))
    q -= 1

