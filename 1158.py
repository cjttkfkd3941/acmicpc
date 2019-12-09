# 1158 조세퍼스 문제
# 링크드 리스트로 구현 가능
n,k = map(int,input().split())
linkedlist = [(i+1) for i in range(n)]
l = []
cnt = 0
idx = 0

while len(linkedlist)!=1:
    if cnt!=k-1:
        cnt +=1
        idx +=1
    else:
        if idx//len(linkedlist)>=1:
            idx %=len(linkedlist)
        n = linkedlist.pop(idx)
        l.append(n)
        cnt = 0
        #print(linkedlist)
l.append(linkedlist.pop())
string = "<"+", ".join(map(str,l))+">"
print(string)