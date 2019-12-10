# 2225 합분해
# k+1차 계차수열(k+1번째 S(n)일수도?)
n,k = map(int,input().split())
l = [[0]*(n+1) for i in range(k)]
l[0] = [1]*(n+1)
for i in range(1,k):
    for j in range(n+1):
        l[i][j] = sum(l[i-1][:j+1])
for i in l:
    print(i)
print(l[-1][-1]%1000000000)

# (n+k-1 choose k-1)
# 
n,k = map(int,input().split())
answer= 1
for i in range(n+1,n+k):
    answer*=i
for j in range(k-1,0,-1):
    answer//=j
print(answer)
