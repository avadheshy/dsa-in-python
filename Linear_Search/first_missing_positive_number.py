"""
The idea is to mark the elements in the array which are greater than N and less than 1 with 1.

Follow the steps below to solve the problem:

The smallest positive integer is 1. First, we will check if 1 is present in the array or not. If it is not present then 1 is the answer.
If present then, again traverse the array. The largest possible answer is N+1 where N is the size of the array. 
When traversing the array, if we find any number less than 1 or greater than N, change it to 1. 
This will not change anything as the answer will always be between 1 to N+1. Now our array has elements from 1 to N.
Now, for every ith number, increase arr[ (arr[i]-1) ] by N. But this will increase the value more than N. So, we will access the array by arr[(arr[i]-1)%N].
We will find now which index has a value less than N+1. Then i+1 will be our answer. 
"""

# Python3 program for the above approach

# Function for finding the first missing
# positive number
def firstMissingPositive(arr, n):

	ptr = 0

	# Check if 1 is present in array or not
	for i in range(n):
		if arr[i] == 1:
			ptr = 1
			break

	# If 1 is not present
	if ptr == 0:
		return(1)

	# Changing values to 1
	for i in range(n):
		if arr[i] <= 0 or arr[i] > n:
			arr[i] = 1

	# Updating indices according to values
	for i in range(n):
		arr[(arr[i] - 1) % n] += n

	# Finding which index has value less than n
	for i in range(n):
		if arr[i] <= n:
			return(i + 1)

	# If array has values from 1 to n
	return(n + 1)

# Driver Code
if __name__ == '__main__':
	# Given array
	A = [0, 10, 2, -10, -20]
	
	# Size of the array
	N = len(A)
	
	# Function call
	print(firstMissingPositive(A, N))

# This code is contributed by shailjapriya
