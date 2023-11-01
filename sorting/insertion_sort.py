"""
start from the second element put this element in the sorted order
"""
def sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        j+=1
        arr[j]=temp
arr=[10,15,20,22,2,4,111,33,2]
sort(arr)
print(arr)