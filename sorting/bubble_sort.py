"""
In each iteration put the largest element from the remaining array at their 
position in the sorted array.
"""
def sort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
arr=[10,15,20,22,2,4,111,33,2]
sort(arr)
print(arr)
                