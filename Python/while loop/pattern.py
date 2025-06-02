n=int(input("enter a number:"))
i=1
while i<=n:
    if i%2==0:
        for j in range(i):
            print(i)
    else:
        print(i)
    i+=1