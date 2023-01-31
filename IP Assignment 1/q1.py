inp=input()
y = [int(x) for x in str(inp)]
# print(y)
z=len(y)
unit_arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
tens_arr=[' ','x','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
if z==1:
    print(unit_arr[y[0]])
elif y[0]==1:
    arr=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
    print(arr[y[1]])
elif z==2:
    unit_arr = ['','one','two','three','four','five','six','seven','eight','nine']
    print(tens_arr[y[0]],end=" ")
    print(unit_arr[y[1]])
# elif z==3:
#     hundredth_arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
#     print(hundredth_arr[y[0]],end=" ")
    

