# Python program to print all Primes Smaller 
# than or equal to N using Sieve of Eratosthenes


def SieveOfEratosthenes(num):
	prime = [True for i in range(num+1)]
    # boolean array
	p = 2
	while (p * p <= num):

		# If prime[p] is not
		# changed, then it is a prime
		if (prime[p] == True):

			# Updating all multiples of p
			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	# Print all prime numbers
	for p in range(2, num+1):
		if prime[p]:
			print(p)


# Driver code
if __name__ == '__main__':
	num = 30
	print("Following are the prime numbers smaller"),
	print("than or equal to", num)
	SieveOfEratosthenes(num)


"""
There is a variation called segmented seive. To solve that there are these 4 steps.
1. Find the all prime le sqrt(R) in prime array.
2. Make a array of lenght R-L+1 make this True.
3. Iterate over each element of prime and make all the multiple of that in range L-R and make Them False.
4. Find all those numbers that are stil True are the required prime numbers.
"""
