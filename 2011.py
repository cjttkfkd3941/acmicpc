# 백준 2011 암호코드 파이썬
# 재귀 시간초과
# def find(s,k,word=[]):
#     cnt = 0
#     #print(s,k,word)
#     if k==0:
#         return 1
#     if s//k==1:
#         cnt+=find(s%k,k//10,word+[s//k])
#         cnt+=find(s%(k//10),k//100,word+[s//(k//10)])
#     elif s//k==2:
#         if s//(k//10)<=26:
#             cnt+=find(s%k,k//10,word+[s//k])
#             cnt+=find(s%(k//10),k//100,word+[s//(k//10)])
#         else:
#             cnt+=find(s%k,k//10,word+[s//k])
#     elif s//k==0:
#         pass
#     else:
#         cnt+=find(s%k,k//10,word+[s//k])
#     return cnt%1000000
# s = int(input())
# k = 10
# while s//k!=0:
#     k*=10
# k//=10
# print(find(s,k))

# cnt(n) : 피보나치n과 값은 같음
cnt = [1,1]+[0]*4999
for i in range(2,5001):
    cnt[i]=cnt[i-1]+cnt[i-2]

# divide=[]

# 3~7으로 끝나는 수를 기준으로 나눔.
# 그러면 각 가지고 있는 값들은 {1 or 2}*(n-1) +  {3~7 or 0}

s = input()
start = 0;check = False
count = 1
for i in range(len(s)):
    if s[i]=="1" or s[i]=="2":
        pass
    elif s[i]=="0":
        if s[i-1]=="1" or s[i-1]=="2":
            end=i
            count*=cnt[end-start-1]
            #divide.append(s[start:end+1])
            start = i+1
        else:
            count = 0
            break
    else:
        end = i
        if s[i] in (list(str(789))) and s[i-1]=="2":
            count*=cnt[end-start]
        else:
            count*=cnt[end-start+1]
        #divide.append(s[start:end+1])
        start = i+1
if s[-1] in ("1","2"):
    end = len(s)-1
    count*=cnt[end-start+1]
    #divide.append(s[start:])
print(count%1000000)
#print(divide)

