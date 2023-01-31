import math
initial_time= int(input("initial time: "))
final_time= int(input("final time : "))
distance=0

while initial_time<=final_time:
    v1=(2000*math.log(140000/(140000-2100*initial_time)))-9.8*initial_time
    initial_time=initial_time+0.25
    v2=(2000*math.log(140000/(140000-2100*initial_time)))-9.8*initial_time

    avg_velocity=(v1+v2)/2
    local_distance=avg_velocity*0.25
    distance=distance+local_distance

print("total distance covered in this interval = ",distance)

