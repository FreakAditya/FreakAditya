dist=1
x=0
y=0
total_distance=0
while(dist!=0):
    inp_dist=int(input())
    if inp_dist<=25:
        y=y+inp_dist
    elif inp_dist>=26 and inp_dist<=50:
        y=y-inp_dist
    elif inp_dist>=50 and inp_dist<=75:
        x=x-inp_dist
    elif inp_dist>=76:
        x=x+inp_dist
    dist=inp_dist
    total_distance=(total_distance+inp_dist)
    
displacement=(x**2+y**2)**(1/2)
    
print("current x coordinate is " ,x)
print("current y coordinate is " ,y)
print(" total distance ", total_distance)
print(" displacement ", displacement)

