arr=[0,1,3]
n=len(arr)

total=n*(n+1)//2

sum=0
for i in arr:
    sum=sum+i
missing=total-sum
print("Missing No:",missing)