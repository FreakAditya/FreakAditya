def f(x):
    return x**3 - 10.5*x**2 + 34.5*x - 35
def diff_f(x):
    return 3*x**2-21*x+34.5

x0=float(input("enter x0: "))
i=1
while(i<=100):
    root=x0-(f(x0)/diff_f(x0))
    if abs(root-x0)<=0.0001: break
    x0=root
    i+=1
print("Root of this equation is: ",round(root,5)," at ",i," itteration.")