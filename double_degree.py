f=open('rosalind_ddeg.txt','r')
n=int(f.readline().split()[0])
d=[0 for i in range (n)]
di=dict ((i,list()) for i in range (n))
for l in f:
    for j in (0,1):
        i=l.split()[j]
        i=int(i)
        d[i-1]=d[i-1]+1
        di[i-1].append(l.split()[1-j])
result=[0 for x in range (n)]
for i in di:
    for j in di[i]:
        result[i]=result[i]+d[int(j)-1]

print ' '.join(map(str,result))