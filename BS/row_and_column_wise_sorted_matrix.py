"""
Search in a row-wise and column-wise sorted matrix in linear time complexity:
The simple idea is to remove a row or column in each comparison until an element is found. Start searching from the top-right corner of the matrix. There are three possible cases:-

The given number is greater than the current number: This will ensure that all the elements in the current row are smaller than the given number as the pointer is already at the right-most elements and the row is sorted. Thus, the entire row gets eliminated and continues the search for the next row. Here, elimination means that a row needs not to be searched.
The given number is smaller than the current number: This will ensure that all the elements in the current column are greater than the given number. Thus, the entire column gets eliminated and continues the search for the previous column, i.e. the column on the immediate left.
The given number is equal to the current number: This will end the search.
"""
def search(mat, n, x):
 
    i = 0
 
    # set indexes for top right element
    j = n - 1
    while (i < n and j >= 0):
 
        if (mat[i][j] == x):
 
            print("Element found at ", i, ", ", j)
            return 1
 
        if (mat[i][j] > x):
            j -= 1
 
        # if mat[i][j] < x
        else:
            i += 1
 
    print("Element not found")
    return 0  # if (i == n || j == -1 )
 
 
# Driver Code
if __name__ == "__main__":
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
 
    # Function call
    search(mat, 4, 29)
"""
This solution runs in O(max(n,m))
"""
"""
There is another variation of the this problem which can be solve i log(max(m,n)). Problem is as follows:
Integers in a row is in increasing order.
first element of arr is greater than last element of previous row
"""
arr=[[1,2,4],
     [5,6,8],
     [10,12,14]
     ]
def solve(arr,k):
    n,m=len(arr),len(arr[0])
    left,right=0,n*m-1
    while left<=right:
        mid=(left+right)//2
        temp=arr[mid//n][mid%n]
        if temp==k:
            print('hey')
            return True
        elif temp>k:
            right=mid-1
        else:
            left=mid+1
    return False

solve(arr,14)
        