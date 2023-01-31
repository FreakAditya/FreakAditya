def profit(M, nt, nc):
    profit = 0
    if nt <= M and nc <= M:
        profit = (90*nt)+(15*nc)
    elif nt <= M and nc > M:
        profit = (90*nt)+(15*M)+(30*(nc-M))
    elif nt > M and nc <= 10:
        profit = (90*M)+((nt-M)*100)+(15*nc)
    else:
        profit = (90*M)+((nt-M)*100)+(15*nc)+(30*(nc-M))

    return profit


x = int(input("Enter the value of M:"))
chair = 2
table = 1
list = []
while(chair != 0):
    chair = 200-(4*table)
    list.append(profit(x, table, chair))
    table += 1
max_profit = max(list)
index_max = list.index(max_profit)
print("No of tables and chair need to manifacture for maximum profit are ",
      index_max+1, " and ", (400-(8*(index_max+1))))
print(max_profit)