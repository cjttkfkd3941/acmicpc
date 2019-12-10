# 2225 합분해
# k+1차 계차수열(k+1번째 S(n)일수도?)

# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

# 입력
# 첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

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
