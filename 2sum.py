def findpair(l,n):
    for i in range(n):
        j=0
        while j<i:
            if l[i]+l[j]==0:
                return ' '.join(map(str,[j+1,i+1]))
            j=j+1
    return (-1)

f=open('rosalind_2sum.txt','r')
l1=f.readline().split()
k=int(l1[0])
n=int(l1[1])
result=[list() for i in range(k)]
for i in range(k):
    l=map(int,f.readline().split())
    result[i]=findpair(l,n)

print '\n'.join(map(str,result))