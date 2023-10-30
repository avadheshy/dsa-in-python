class Solution:
    def isPossible(self,arr,k,mid):
        count=1
        total=0
        for i in range(len(arr)):
            if total+arr[i]<=mid:
                total+=arr[i]
            else:
                count+=1
                if count>k or arr[i]>mid:
                    return False
                total=arr[i]
        return True
    def splitArray(self, nums, k) -> int:
        start,end,ans=0,sum(nums),-1
        while start <= end:
            mid=(start+end)//2
            if self.isPossible(nums,k,mid):
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans