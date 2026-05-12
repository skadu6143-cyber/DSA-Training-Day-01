cp=int(input("Enter Cost Price :"))
Student=input("Are you Student? Y/N :")

if Student=="Y":
    print("User is Student")
    
    if cp>500:
        TD=cp*(10/100)
    else:
        TD=cp*(5/100)
    print("Total Discount",TD)
else:
    print("User is not Student")
    
    if cp>500:
        TD=cp*(8/100)
    else:
        TD=cp*(2/100)
    print("Total Discount",TD)
