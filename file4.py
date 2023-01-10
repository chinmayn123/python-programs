mynum = int(input("Enter Number: "))

if (mynum < 0):
    print("Negative number")
elif (mynum <= 9):
    print("1 digit")
elif(mynum <= 99):
    print("2 digit")
elif(mynum <= 999):
    print("3 digit")
elif (mynum > 999):
    print("more than 3 digit")
else:
    print("negative number")

