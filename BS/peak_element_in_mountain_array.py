arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def peakIndexInMountainArray(A) -> int:
    lo, hi = 0, len(A)-1
    while lo < hi:
        mid = (lo+hi)//2
        if A[mid] > A[mid+1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


"""
This code will print the index of that element in the array
Binary search on the "lower boundary of A[i]>A[i+1]A[i] > A[i+1]A[i]>A[i+1]" instead of A[i−1]<A[i]>A[i+1]A[i-1] < A[i] > A[i+1]A[i−1]<A[i]>A[i+1].
"""
"""
Approach
The approach used to solve this problem is binary search. We start by setting left and right pointers to the start and end of the array, respectively. We then enter a while loop that continues until left is not less than right. Within this loop, we calculate the middle index, mid, of the current subarray.

We check if the element at mid is less than the element at mid + 1. If it is, this means that we're still in the ascending part of the array, and hence, the peak is somewhere to the right of mid. So, we update left to mid + 1.

If the element at mid is not less than the element at mid + 1, it means we've crossed the peak and are now in the descending part of the array. Hence, the peak is somewhere to the left of mid. So, we update right to mid.

This process continues, reducing the search space by half in each iteration, until left is not less than right. At this point, left will be pointing to the peak of the mountain, and that's what we return.

Complexity
Time complexity: The time complexity for this approach is (O(\log n)), where (n) is the length of the array. This is because with each iteration, we are effectively reducing the search space by half, which is a characteristic of binary search.

Space complexity: The space complexity is (O(1)), as we are using a constant amount of space to store our variables left, right, and mid.
"""
print(peakIndexInMountainArray(arr))
