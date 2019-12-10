# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

# 출력
# 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

# A1x1+A2x2+...+Akxk=d(A1,A2,...,Ak는 상수)
# 를 만족하려면 d는 x1,x2,...xk의 공약수 의 배수일 경우만 가능(Diophantine Equation)

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
