import math
def pop_after_n_years(pop,rate):
    new_pop=0
    year=1
    last=1
    second_last=0
    while(last>second_last):                                                  # 7900  8574, 13 
        second_last=pop
        population_changed=(pop*rate)/100
        new_pop=pop+population_changed
        pop=new_pop
        rate=rate-0.1
        last=pop
        year+=1
    print("group will reach max population in ",year,"year.")
    print("Max population in ",year,"year will be: ",int(pop),"million")
    return pop

pop = [7900]
rate=2.5
number=1
total_population=0
for i in pop: 
    print("for group",number)
    # pop_after_n_years(i,rate)
    total_population=total_population+pop_after_n_years(i,rate)
    # rate=rate-0.4
    # number+=1

print("total population of world will be : ",int(total_population),"million")



