# --------------------Q1(a)----------------
# i = 1
# evenList = []
# while i <= 10:
#     if (i % 2 == 0):
#         evenList.append(i)
#     i += 1
#
# print(evenList)

# ----------------------Q1(b)----------------
# i = 1
# oddList = []
# while i <= 10:
#     if (i % 2 != 0):
#         oddList.append(i)
#     i += 1
#
# print(oddList)

# -----------------------Q1(c)------------------
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# ------------------------Q1(d)-----------------
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# -----------------------Q2-----------------------
# i = 1
# while i <= 10:
#     print(f"{i} = {i*i}")
#     i += 1

# ------------------------Q3----------------------
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# -----------------------Q4------------------------
flag = 0
# n = int(input('Enter whole number to check : '))
# i = 2
# while i <= (n / 2):
#     if (n % i) == 0:
#         flag = 1
#         break
#     else:
#         i += 1
#
# if n == 1:
#     print('1 is neither prime nor composite')
# elif flag == 0:
#     print(n, ' is a prime number.')
# elif flag == 1:
#    print(n, ' is not a prime number.')

# -----------------------Q5--------------------
# n = int(input("Enter the nth value: "))
# a = 0
# b = 1
# sum = 0
# print("Fibonacci Series : ", end = " ")
# while(sum <= n):
#      print(sum, end = " ")
#      a = b
#      b = sum
#      sum = a + b

# ---------------------Q6--------------------
# n = int(input("Enter the number: "))
# num = 1
# while n >= 1:
#     num = num * n
#     n = n - 1
#
# print(num)

# --------------------Q7--------------------
# num = int(input("Enter a Number:"))
# order = len(str(num))
# temp = num;
# sum = 0
# while(temp>0):
#     digit =temp%10
#     sum += digit **order
#     temp = temp//10
# if(sum==num):
#     print("",num,"is an Armstrong number")
# else:
#     print("",num,"is not an Armstrong number")

