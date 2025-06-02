#for i in range(1,11):
#     print(i)

# def natural(a,b):
#     for a in range(1,b):
#         print(a)
# natural(1,11)

# for i in range(2,21,2):
#     print(i)

# def even(a,b):
#     for a in range(a,b):
#         if a%2==0:
#             print(a)
# even(2,21)

# s = "python"
# for i in s:
#     print(i)

# def string():
#     s="python"
#     for i in s:
#         print(i)
# string()

# s=0
# for i in range(1, 101):
#     s+=i
# print(s)

# def sum():
#     s=0
#     for i in range(1, 101):
#         s+=i 
#     print(s)
# sum()

# i=int(input( ))
# for j in range(1,11):
#     print(i,'*',j,'=',i*j)

# def table(i,j,k):
#     for j in range(i,j):
#         print(k,'*',j,'=',k*j)
# table(1,11,5)


# l= ["apple", "banana", "cherry"]
# for i in l:
#     print(i)

# def list():
#     l=["apple", "banana", "cherry"]
#     for i in l:
#         print(i)
# list()


# def vowels():
#     s="education"
#     v="aeiou"
#     for char in s:  #education
#         if char in v: #aeiou
#            print(char)
# vowels()

# def vowels(s,v):
#     for char in s:  #education
#         if char in v: #aeiou
#            print(char)
# vowels(s="education",
#     v="aeiou")


# s="education"
# v="aeiou"
# for char in s:  #education
#     if char in v: #aeiou
#         print(char)


# Count how many times the letter 'a' appears in the string "banana" using a loop.

# s='banana'
# count=0
# for i in s:
#     if i=='a':
#         count+=1
# print(count)

# def c(s,count):
#     for i in s:
#         if i=='a':
#             count+=1
#     print(count)
# c(s='banana',
# count=0)

# Print numbers from 10 to 1 using a loop (reverse order).

# for i in range(10,0,-1):
#     print(i)


# def reverse(a,b,c):
#     for i in range(a,b,c):
#         print(i)
# reverse(10,0,-1)

# n = int(input())
# sum = 0
# for i in range(1, n):
#     sum += i
# print(sum)

def s(sum, n):
    for i in range(1, n): 
        sum += i
    print(sum)

s(0, 6)  
