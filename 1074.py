# 1074 Z

# r,c>1이면 앞선 앞선 숫자들은 크기를 줄이면서 counting
n,r,c = map(int,input().split())
length = 2**n
cnt = 0
while r>1 or c>1:
    if r>=length//2:
        r-=length//2
        cnt += (length**2)//2
    if c>=length//2:
        c-=length//2
        cnt += (length**2)//4
    length//=2
print(2*r+c+cnt)