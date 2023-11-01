"""
1. Boyer-Moore Majority Voting Solution
Create variables to track counts and candidates for potential majority elements.
First Pass - Find Potential Majority Elements:
Iterate through the input array and identify potential majority element candidates.
Update the candidates based on specific conditions.
Maintain counts for each candidate.
Second Pass - Count Occurrences:
Iterate through the input array again to count the occurrences of the potential majority elements.
Compare the counts with a threshold to determine the majority elements.
Return Majority Elements.
"""
#There will be at most 2 majority element
def majorityElement(nums):
    count1,count2,ele1,ele2=0,0,0,0
    for i in nums:
        if i==ele1:
            count1+=1
        elif i==ele2:
            count2+=1
        elif count1==0 and i!=ele2:
            count1=1
            ele1=i
        elif count2==0 and i!=ele1:
            count2=1
            ele2=i
        else:
            count1-=1
            count2-=1
    th=len(nums)//3
    count1=count2=0
    for i in nums:
        if i==ele1:
            count1+=1
        elif i==ele2:
            count2+=1

    ans=[]
    if count1>th:
        ans.append(ele1)
    if count2>th:
        ans.append(ele2)
    return ans