#Динамика по ценности


N, M = [int(i) for i in input().split()]
weights = [int(i) for i in input().split()]
costs = [int(i) for i in input().split()]
COST = sum(costs)
y = [[0 for i in range(COST+1)] for j in range(N+1)]
for i in range(1, COST+1):
    y[0][i] = M + 1


for i in range(1,N+1):
    for V in range(COST+1):
        
        if costs[i-1] > V:
            y[i][V] = y[i-1][V]
        else:
            y[i][V] = min(y[i-1][V], y[i-1][V-costs[i-1]] + weights[i-1])
#Построили матрицу y[i,V]
#где i -  используем до i-го предмета
#V - стоимость которуюю набирвем





IND = COST
while y[N][IND] == M+1:
    IND-=1
#IND - максимальная цена, которую можно набрать используя все предметы






lis =[]
for i in range(N, -1,-1):
    if y[i-1][IND] != y[i][IND]:
        lis.append(i)
        IND-=costs[i-1]



for i in lis:
    print(i)