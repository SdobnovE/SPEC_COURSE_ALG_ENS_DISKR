#Динамика по весам



N, M = [int(i) for i in input().split()]
weights = [int(i) for i in input().split()]
costs = [int(i) for i in input().split()]

c = [0 for i in range(M+1)]
lists = [[] for i in range(M+1)] 
c[0] = 0

for W in range(1, M+1):
    c[W] = c[W-1]
    lists[W] = lists[W-1]
        
    for i in range(N):
        w = weights[i]
        if W - w >= 0 and  i not in lists[W-w]:
                if c[W] < costs[i] + c[W-w]:
                    lists[W] = lists[W-w] + [i]
                    c[W] = costs[i] + c[W-w]
print(c[M])

