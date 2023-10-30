arr = [4, 5, 6, 7, 8, 9, 10, 11, 1,2,3]

"""
The first element will be always greater the pivot element
we can find which side of the mid element the pivot is exists. 
If mid is greater than the first element of the array then we are in 
increasing part of the array else we are in decreasing part of the array.
"""
def pivot(arr):
        i,j=0,len(arr)-1
        while(i<j):
            m=(i+j)//2
            if arr[m]>=arr[0]:
                i=m+1
            else:
                j=m
        return i



print(pivot(arr))