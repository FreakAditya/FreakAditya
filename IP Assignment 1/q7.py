def saving(A, sf, IR, n):
    your_saving = A*sf
    balance = your_saving
    for i in range(n):
        interest = (balance*IR)/100
        balance = balance+interest+your_saving
    return balance-your_saving


allowance = 20000
saving_fraction = 0.1
interest_rate = 0.5

# print(round(saving(allowance, saving_fraction, interest_rate, no_of_month)),2)
 
cost_of_laptop = float(input("enter the cost of laptop : "))
mybal = 0
n = 1
while(mybal < cost_of_laptop):

    mybal = saving(allowance, saving_fraction, interest_rate, n)
    n += 1

print("no of month he need to wait: ",n-1)
# print(round((mybal)-cost_of_laptop),2)      10000,   100.5
mybal = saving(allowance, saving_fraction, interest_rate, n-1)
print(mybal-cost_of_laptop)


