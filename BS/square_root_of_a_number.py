def floorSqrt(n):
   # write your code logic here .
   i,j,ans=0,n,0
   while i<j:
      m=(i+j)//2
      if m*m<=n:
         ans=m
         i=m+1
      elif m*m>n:
         j=m-1
      else:
         i=m+1
      return ans
n= int(input())
print(floorSqrt(n))