coordinate = int(input("No of corrdinate: "))
list1 = []
list2 = []
final = []
sum = 0
print("Enter Comma Seprated Coordinates ")
for i in range(coordinate):
    val = input()
    tup = tuple(int(item) for item in val.split(','))
    # tup=tuple(input().split(','))
    list1.append(tup+(0,))
print("enter scaling parameter")
cx = int(input("Cx: "))
cy = int(input("Cy: "))

list2.append((cx, 0, 0))
list2.append((0, cy, 0))
list2.append((0, 0, 1))

for i in range(len(list1)):
    for j in range(len(list2)):
        for k in range(len(list2)):
            sum = sum+(list1[i][k])*list2[k][j]
        final.append(sum)
        sum = 0
    # not storing the resultant coordinates,directly printing
    print("Coordinate", i+1, "of resultant shape is ", end=" ")
    print(final[0], end=",")
    print(final[1])
    final.clear()

# print(list1)
# print(list2)
# print(final2)
