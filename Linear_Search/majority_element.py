"""
Moore’s Voting Algorithm:
This is a two-step process:
The first step gives the element that may be the majority element in the array. 
If there is a majority element in an array, then this step will definitely return majority
element, otherwise, it will return candidate for majority element.
Check if the element obtained from the above step is the majority element. 
This step is necessary as there might be no majority element. 
"""

# Program for finding out majority element in an array

# Function to find the candidate for Majority


def findCandidate(A):
	maj_index = 0
	count = 1
	for i in range(len(A)):
		if A[maj_index] == A[i]:
			count += 1
		else:
			count -= 1
		if count == 0:
			maj_index = i
			count = 1
	return A[maj_index]

# Function to check if the candidate occurs more than n/2 times


def isMajority(A, cand):
	count = 0
	for i in range(len(A)):
		if A[i] == cand:
			count += 1
	if count > len(A)/2:
		return True
	else:
		return False

# Function to print Majority Element


def printMajority(A):
	# Find the candidate for Majority
	cand = findCandidate(A)

	# Print the candidate if it is Majority
	if isMajority(A, cand) == True:
		print(cand)
	else:
		print("No Majority Element")


# Driver code
A = [1, 3, 3, 1, 2,3,3]

# Function call
printMajority(A)
