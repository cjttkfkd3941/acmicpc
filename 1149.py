#1149 RGB거리
# lr,lg,lb : 마지막 red,green,blue를 선택한 값중 가장 작은값을 저장한 배열
# lr,lg,lb중 가장 작은 값
n = int(input())
r,g,b=map(int,input().split())
lr = [r]
lg = [g]
lb = [b]
s = [min(r,g,b)]
for i in range(1,n):
    r,g,b=map(int,input().split())
    lr.append(min(lg[i-1]+r,lb[i-1]+r))
    lg.append(min(lr[i-1]+g,lb[i-1]+g))
    lb.append(min(lr[i-1]+b,lg[i-1]+b))
    s.append(min(lr[i],lg[i],lb[i]))
    

print(s[n-1])
