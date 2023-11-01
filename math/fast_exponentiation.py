

# Iterative Function to calculate (x^y)%p in O(log y)
def power(x, y, p):
 
    # Initialize result
    res = 1
 
    while (y > 0):
 
        # If y is odd, multiply x with result
        if ((y & 1) != 0):
            res = res * x
 
        # y must be even now
        y = y >> 1  # y = y/2
        x = x * x  # Change x to x^2
 
    return res % p
 
  # Driver Code
 
 
x = 2
y = 5
p = 13
print("Power is ", power(x, y, p))
# This code is contributed by Khushboogoyal499