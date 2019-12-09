n,k = map(int,input().split())
l = []
for i in range(n):
    t = int(input())
    if t<=k:
        l.append(t)
    else:
        n-=1
ind = 1
t1 = l[0]
while ind<n:
    t2 = l[ind]
    while t1!=0:
        t1,t2 = t2%t1,t1
    #print(t1,t2)
    t1 = t2
    ind+=1
if k%t1!=0:
    print(-1)
else:
    ll = [[0]*(k+1) for i in range(n)]
    # for i in range(n):
    #     ll[i][0] = 1
    for p in range(0,k+1,l[0]):
        ll[0][p] = p//l[0]
    for i in range(1,n):
        for j in range(1,l[i]):
            ll[i][j] = ll[i-1][j]
        ll[i][l[i]] = 1
        for j in range(l[i]+1,k+1):
            ll[i][j] = min(ll[i][j-l[i]]+1 if ll[i][j-l[i]]!=0 else 10000,ll[i-1][j-l[i]]+1 if ll[i-1][j-l[i]]!=0 else 10000,ll[i-1][j] if ll[i-1][j]!=0 else 100000)
    minima = 10000
    # for i in ll:
    #     print(i)
    for i in range(n):
        if minima>ll[i][-1] and ll[i][-1]!=0:
            minima = ll[i][-1]
    print(minima)