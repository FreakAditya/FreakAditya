def factorial(x):
    if x == 0:
        return 1
    if x > 0:
        x = x * factorial(x-1)
    return x


def sin(x):
    value = 0
    for i in range(60):

        sign = (-1)**i

        pi = 3.14

        y = x*(pi/180)

        value = value + ((y**(2.0*i+1))/factorial(2*i+1))*sign

    return value

def cos(x):
    return ((1-sin(x)**2)**(1/2))

def tan(x):
    return sin(x)/cos(x)

x = int(input("enter angle in degree: "))
n = float(input("enter base distance: "))

# print(sin(x),cos(x),tan(x))

height_of_pole=tan(x)*n
hypotenus=n/cos(x)

print("height : ",round(height_of_pole,2))
print("slant distance= ", round(hypotenus,2))

