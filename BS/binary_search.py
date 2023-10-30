arr=[1,2,3,4,5,6,7,8,9,10]
def search(arr,t):
    i,j=0,len(arr)-1
    while i<=j:
        m=(i+j)//2
        if arr[m]==t:
            return m
        elif arr[m]>t:
            j=m-1
        else:
            i=m+1
    return -1
"""
This code will print the index of that element in the array"""
print(search(arr,11))