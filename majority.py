class major_list(list):
    def find_major(self,n):
        element=self[0]
        vote=1
        for candidate in self[0:]:
            vote+=[-1,1][candidate==element]
            if vote==0:
                element = candidate
                vote=1
        return [-1,element][self.count(element)>n/2]



f=open('rosalind_maj.txt')
l1=f.readline().split()
k=int(l1[0])
n=int(l1[1])
i=0
result=[0 for j in range(k)]
for line in f:
    result[i]=major_list(map(int,line.split())).find_major(n)
    i=i+1

print ' '.join(map(str,result))
