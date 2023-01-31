f=open("file3.txt",'r')
name=[]
sign=[]
for line in f:
    l=line.split()
    # print(l)
    if len(l)==1:
        name.append(l[0].replace(':',''))
        sign.append(sum)
        sum=0
    else:
        sum=sum+int(l[1])
sign.append(sum)
# print(name)
del sign[0]
# print(sign)
# print(max(sign),min(sign))
print("Maximum no of signature done by: ", end=' ')
for i in range(len(sign)):
    if sign[i]==max(sign):
        print(name[i],end=' ')
print()
print("Minimum no of signature done by: ", end=' ')
for j in range(len(sign)):
    if sign[j]==min(sign):
        print(name[j],end=' ')


