#1010 다리 놓기
# 다리가 겹칠수 없다.
# 동쪽의 m개에서 n개 뽑는경우 서쪽의 n개에 차례대로 선택 되면 겹쳐지지않는다.
# 따라서 a Choose b
n = int(input()) #입력받을 횟수
for time in range(n):
    #b:서쪽의 시작점의 갯수,a : 동쪽의 다리가 놓아질수 있는 위치의 갯수
    b,a = map(int,input().split())
    b = max(b,a-b)
    b_ = min(b,a-b)
    sol = 1
    while a!=b:
        sol *=a
        a-=1
        #print(f"sol={sol},a={a}")
    while b_!=0:
        sol//=b_
        b_-=1
        #print(f"sol={sol},b={b}")
    print(sol)