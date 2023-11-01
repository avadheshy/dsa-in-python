"""
In each iteration find the index of the smallest element in the array and 
put it at its position.
"""
def sort(arr):
    for i in range(len(arr)):
        index=i
        temp=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<temp:
                temp=arr[j]
                index=j
        arr[i],arr[index]=arr[index],arr[i]
arr=[10,15,20,22,2,4,111,33,2]
sort(arr)
print(arr)