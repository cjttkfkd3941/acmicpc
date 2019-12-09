# 1024 수열의 합

a,b = map(int,input().split()) # a : 합의 크기, n : 합이 될 수열의 최소 갯수
for i in range(b,101):
    if i%2==1: 
    # 갯수가 홀수개라면, 평균 기준으로 (-k,-k+1,...,0,...,k-1,k) 로 표현가능.
    # 즉 중앙값*i
        if a%i==0 and a//i-i//2>=0:
            print(" ".join(map(str,[a//i+j-i//2 for j in range(i)])))
            break
    else:
    # 짝수일 경우, (2**k)*p 로 만들어서 k 를 탐색
    # k가 1 이면 , a가 홀수만 가능
    # k가 2 이면, a는 2의 배수이지만 4의 배수는 불가능
    # k가 n 이면, a는 2^(n-1)의 배수이지만,2^n은 불가능
        check = 1
        while i%(2**(check+1))==0:
            check+=1
        if a%(2**(check-1))==0:
            k = (a//(i//2)-1)//2
        else:
            continue
        if (2*k+1)*(i//2)!=a:
            continue
        if k-i//2+1>=0:
            print(" ".join(map(str,[k-i//2+1+j for j in range(i)])))
            break
else:
    print(-1)