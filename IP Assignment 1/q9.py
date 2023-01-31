import math


def demand(p):
    a = 10
    b = 1.05

    demand_price = math.exp(a - b*p)

    return demand_price


def supply(p):
    c = 1
    d = 1.06

    supply_price = math.exp(c + d*p)

    return supply_price


min_price = 1
while(supply(min_price) < demand(min_price)):
    # min_price = min_price+(min_price*(5/100))
    min_price = min_price + 0.05           

print("Price of equilibrium is: ", round(min_price, 2))
print("Demand at this price: ", round(demand(min_price), 2))
print("Supply at this price: ", round(supply(min_price), 2))
