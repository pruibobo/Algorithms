# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def search(l:list,val):
    n=len(l)
    for i in range(n):
        if l[i]==val:
            return i
    else:
        return None

def binary_search(l:list,val): # list must be sorted
    left=0
    right=len(l)-1
    for i in range(len(l)):
        mid=(left+right)//2
        if l[mid]==val:
            return mid
        elif l[mid]>val:
            right=mid-1
        else:
            left=mid+1
    else:
        return None

l=[1,2,3,4,5,6,7,8,9,0]
print(search(l,3))
print(binary_search(l,4))



