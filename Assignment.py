# -----------Q1---------------
# list1=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in list1:
#     sum+=i
#
# print(sum)

# -----------Q2---------------
# x = int(input("Enter Number: "))
#
# for i in range(0, 10):
#     print(str(x) + " * " + str(i+1) + " = " + str((i + 1) * x))


# -----------Q3---------------
# for i in range(10):
#     print(i+1)

# ----------Q4---------------
#  list1 = [1,2,3,4,5,6,7,8,9]
# evenList = []
# oddList = []
#
# for i in list1:
#     print(i)
#     if(i%2==0):
#         evenList.append(i)
#     else:
#         oddList.append(i)
#
# print(evenList)
# print(oddList)

# -------------Q5-----------
# x = [2,3,4,5,6,7,8]
# sqr = []
# for i in x:
#     sqr.append(i*i)
#
# print(sqr)

# -------------Q6----------
# num = 4
#
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# ----------------Q7-------------
# x = [2,3,4,5,6,7,8]
# sqr = []
# for i in x:
#     sqr.append(i*i)
#
# print(sqr)

# ---------------Q8---------------
# evenList = []
# oddList = []
# for i in range(1, 101):
#     if (i % 2 == 0):
#         evenList.append(i)
#     else:
#         oddList.append(i)
#
# print(evenList)
# print(oddList)

# --------------Q9-------------
# x = [2,3,4,5,6,7,8]
# sqr = []
# for i in x:
#     sqr.append(i*i)
#
# print(sqr)

# -----------Q10-----------
# x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
# positive = []
# negative = []
#
# for i in x:
#     if (i < 0):
#         negative.append(i)
#     else:
#         positive.append(i)
#
# print(positive)
# print(negative)

# ----------------Q11-----------------
# dic = {"val1":10, "val2":20, "val3":23, "val4":22 }
# list1 = []
# for x in dic:
#     if(dic[x]%2==0):
#         list1.append(dic[x])
# print(list1)

# -------------Q12------------
# num = 1
# for i in range(0, 5):
#     for j in range(0, i + 1):
#         print(num, end=" ")
#
#     num = num + 1
#     print("\n")

# ------------Q13------------
# rows = 5
# b = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r')