arr=[3,2,3,1,2,4]
ans=[]

for i in range(len(arr)):
    if arr[i] not in ans:
        ans.append(arr[i])
print(ans)
