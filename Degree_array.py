f=open('rosalind_deg.txt','r')
l1=list(f.readline().split())
nnode=int(l1[0])
result=[0 for x in range (nnode)]
for j in f:
    for i in list(j.split()):
        i=int(i)
        result[i-1]+=1

print str(result).replace(',','').replace('[','').replace(']','')

