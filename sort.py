'''
Low B 三人组： bubble selection insertion
NB 三人组: fast
'''
import heapq
import random

def bubble_sort(l:list):
    n=len(l)
    for i in range(n):
        exchange=False  # stop the loop if l is sorted
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                exchange=True

        if not exchange:
            return

def select_sort_simple(l:list):
    n = len(l)
    for i in range(n-1):
        minpos = i
        for j in range(i+1,n):
            if l[j] < l[minpos]:
                minpos = j
        l[i],l[minpos]=l[minpos],l[i]

    return l

def insert_sort(l:list):
    for i in range(1,len(l)):
        tmp=l[i]
        j=i-1
        while j >= 0 and l[j] > tmp:
            l[j+1]=l[j]
            j -= 1

        l[j+1]=tmp

def partition(l,left,right):
        tmp=l[left]
        while left < right:
            while left < right and l[right] >= tmp:
                right -= 1
            l[left]=l[right]

            while left < right and l[left] <= tmp:
                left +=1
            l[right]=l[left]
        l[left] = tmp
        return left

def quick_sort(l,left,right):
    if left < right:
        mid=partition(l,left,right)
        quick_sort(l,left,mid-1)
        quick_sort(l,mid+1,right)

def sift(l:list,low,high):
    '''
    :param l: list
    :param low: first element of the heap
    :param high: last element of the heap
    :return: list
    '''
    i = low  # i,j are two position pointers
    j = 2 * i + 1 # default as left branch
    tmp = l[low]
    while j <= high : # i is the last layer of parent node
        if j+1 <= high and l[j+1] > l[j]:
            j = j + 1  # j points to the right branch
        if l[j] > tmp:œ
            l[i] = l[j]
            i = j
            j = 2 * i + 1
        else:      # tmp -> parent node
            break
    else:
        l[i] = tmp # tmp -> leaf node

def heap_sort(l):
    n = len(l)
    for i in range((n-2)//2,-1,-1):  # i -> parent node
        sift(l,i,n-1)
    # build a heap
    for i in range(n-1,-1,-1): # i -> last element of the heap
        l[0],l[i] = l[i],l[0]
        sift(l,0,i-1)

def merge(l:list,low,high,mid):
    i=low
    j=mid+1
    tmp=[]
    while i<=mid and j<=high:
        if l[i]<l[j]:
            tmp.append(l[i])
            i+=1
        else:
            tmp.append(l[j])
            j+=1
    while i<=mid:
        tmp.append(l[i])
        i+=1
    while j<=high:
        tmp.append(l[j])
        j+=1
    l[low:high+1]=tmp

def merge_sort(l,low,high):
    if low < high:
        mid=(low+high)//2
        merge_sort(l,low,mid)
        merge_sort(l,mid+1,high)
        merge(l,low,high,mid)

def radix_sort(l):
    max_num=max(l)

l=list(range(100))
random.shuffle(l)
print(l)
merge_sort(l,0,99)
print(l)