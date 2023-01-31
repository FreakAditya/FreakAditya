x=int(input())
s=x
for i in range(x):
    for j in range(i+1):
        print("*",end="")
    for k in range(2*s-2):
        print(" ",end="")

    for l in range(i+1):
        print("*",end="")
        
    s=s-1
    print()