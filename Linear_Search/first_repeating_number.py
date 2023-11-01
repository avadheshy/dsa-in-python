"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space."""
"""
treat each element as array index and make value at this index negative if it occures 
again in the array the its index value is already negative which means this number is 
reapting
"""
def findDuplicate(self, nums) -> int:
    for i in nums:
        indx=abs(i)-1
        if nums[indx]<0:
            return abs(i)
        nums[indx]*=-1