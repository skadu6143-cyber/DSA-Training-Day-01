no=int(input("Enter no:"))
sum=0
count=0
save=no
while no>0:
    no=no//10
    count=count+1
no=save
while no>0:
    rem=no%10
    sum=sum+(rem**count)
    no=no//10
if sum==save:
    print("No is Armstrong")
else:
    print("No is not Armstrong")

