####14501번
#우선순위큐에 넣어서 하루하루 업데이트
#들어갈때는 (그 일이 끝나는 날,그날까지 총 pay에 그 일을 실행할시의 페이)  형식
#우선순위 큐에 들어가므로 먼저끝나는일이 먼저 빠짐
#일이 하나 끝날때마다 그날까지의 최대 
from queue import PriorityQueue
n = int(input())
l = [(0,0)]
sol = PriorityQueue()
tomax = 0
for i in range(n):
    l.append(tuple(map(int,input().split())))
#print(l)
for i in range(1,n+1):
    sol.put(tuple([i+l[i][0]-1,l[i][1]+tomax]))
    #시행
    #print(f"시행{i}: ",sol.queue)
    while sol.queue:
        if sol.queue[0][0]==i:
            work = sol.get()
            if work[1]>tomax:
                tomax = work[1]
        else:
            break
print(tomax)





####14502번
#func함수:l = 기둥이 3개 추가 설치된 상태의 2차원 배열,rem:바이러스의 좌표
#바이러스는 bfs로 확산, 바이러스가 확산되어있으면 시행하지 않음
#확산 시행 후, 문제없는 공간 count
from collections import deque
from copy import deepcopy
n,m = map(int,input().split())
def func(l,rem):
    rem = deque(rem)
    while rem:
        i,j = rem.popleft()
        if l[i][j]==0:
            l[i][j] = 2
        elif l[i][j] == 1:
            continue
        if i<n-1:
            if l[i+1][j]!=2:
                rem.append((i+1,j))
        if i>0:
            if l[i-1][j]!=2:
                rem.append((i-1,j))
        if j<m-1:
            if l[i][j+1]!=2:
                rem.append((i,j+1))
        if j>0:
            if l[i][j-1]!=2:
                rem.append((i,j-1))
    cnt = 0
    for i in range(n*m):
        r,c = i//m,i%m
        if l[r][c]==0:
            cnt+=1
    return cnt
#빈공간중 3개를 기둥으로 변환해서 시행, 전체사건 조사
l = []
rem = []
max = 0
for i in range(n):
    l.append(list(map(int,input().split())))
    for j in range(m):
        if l[i][j]==2:
            rem.append((i,j))
ll = l.copy()
for i in range(n*m):
    ir,ic = i//m,i%m
    if l[ir][ic]==1 or l[ir][ic]==2:
        continue
    else:
        ll[ir][ic]=1
    for j in range(i,n*m):
        jr,jc = j//m,j%m
        if l[jr][jc] ==1 or l[jr][jc] ==2:
            continue
        else:
            ll[jr][jc] = 1
        for k in range(j,n*m):
            kr,kc = k//m,k%m
            if l[kr][kc] ==1 or l[kr][kc] ==2:
                continue
            else:
                ll[kr][kc] = 1
            count = func(deepcopy(ll),rem)#pass by value 로 실행하기 위해서
            if max<count:
                max = count
            ll[kr][kc] = 0
        ll[jr][jc] = 0
    ll[ir][ic] = 0
print(max)
