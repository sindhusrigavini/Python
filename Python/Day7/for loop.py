# sum of odd numbers, from 1 to 10?

# sum=0
# for i in range(1,10,2):
#         sum+=i
# print(sum)

# =================================

# def odd(a,b,c,sum):
#     for i in range(a,b,c):
#         sum+=i
#     print(sum)
# odd(1,10,2,0)

# Sum of even numbers from 1 to 10?

# sum=0
# for i in range(2,10,2):
#         sum+=i
# print(sum)

# =================================

# def even(a,b,c,sum):
#     for i in range(a,b,c):
#         sum+=i
#     print(sum)
# even(2,10,2,0)

#  sum of numbers from 1 to 10?

# sum=0
# for i in range(1,10):
#         sum+=i
# print(sum)

# =================================

# def sum(a,b,c):
#     for i in range(a,10):
#         c+=i
#     print(c)
# sum(1,10,0)

#  Find the Greatest of two numbers

# a=10
# b=20
# if a>b:
#     print('a is greater')
# else:
#     print('b is greater')

# =====================================

# def greater(a,b):
#     if a>b:
#         print('a is greater')
#     else:
#         print('b is greater')
# greater(1000,2500)
# greater(25000,10000)

# Find the Greatest of three numbers

# a=10
# b=20
# c=30
# if a>b and a>c:
#     print('a is greater')
# elif b>a and b>c:
#     print('b is greater')
# else:
#     print('c is greater')

# ===================================

# def greater(a,b,c):
#     if a>b and a>c:
#         print('a is greater')
#     elif b>a and b>c:
#         print('b is greater')
#     else:
#         print('c is greater')
# greater(1000,2500,500)

# print 1 to 10 Prime numbers

# r = 15  
# for n in range(0, r+1):
#     count = 0
#     for i in range(1, n+1): 
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print(n, "is Prime")
#     else:
#         print(n, "is Not Prime")

# ===================================

# def prime(r,count):
#     for n in range(0, r+1):
#         count = 0
#         for i in range(1, n+1): 
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n, "is Prime")
#         else:
#             print(n, "is Not Prime")
# prime(20,0)

# Find the Leap Year

# x=int(input('Enter the year: '))
# if (x%400==0) or (x%4==0 and x%100!=0):
#     print('leap year')
# else:
#     print('not leap year')

# ===================================
# def year(x):
#     print(x)
#     if (x%400==0) or (x%4==0 and x%100!=0):
#         print('leap year')
#     else:
#         print('not leap year')
# year(2025)